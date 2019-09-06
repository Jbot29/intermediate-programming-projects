#lang racket

(require gregor) ;;https://docs.racket-lang.org/gregor/index.html

(struct date-range (start-date end-date value))

(define parse-date-string (curryr parse-datetime  "yyyy-MM-dd'T'HH:mm"))

(define (display-date date)
  (displayln (~t date "yyyy-MM-dd HH::mm")))

(define (display-date-range dr)
  (displayln "\nDate Range\n")
  (display-date (date-range-start-date dr))
  (display-date (date-range-end-date dr))
  (displayln (format "Value ~a" (date-range-value dr))))

(define (display-date-ranges drs)
  (for ([dr drs])
    (display-date-range dr)))

(define (in-range? date dr)
  (and (datetime>=? date (date-range-start-date dr))
       (datetime<=? date (date-range-end-date dr))))

;;reduce to one function? pass in comparision functions and make curry
(define (compare? dr1 dr2 fn1 fn2)
  (and
   (fn1 (date-range-start-date dr1) (date-range-start-date dr2))
   (fn2 (date-range-end-date dr1) (date-range-end-date dr2))))

(define identical? (curryr compare? datetime=? datetime=?))
(define contained? (curryr compare? datetime>=? datetime<=?))


(define (new-date-range new-dr dr2 begin-or-end)
  (if (eq? 'end begin-or-end)
      (date-range (date-range-start-date dr2) (date-range-start-date new-dr) (date-range-value dr2))
      (date-range (date-range-end-date new-dr) (date-range-end-date dr2) (date-range-value dr2))))

(define (overlap-after-current? new-dr current-dr)
  (and
   (datetime<? (date-range-start-date new-dr) (date-range-end-date current-dr))
   (datetime>? (date-range-end-date new-dr) (date-range-end-date current-dr))))

(define (overlap-before-current? new-dr current-dr)
  (and
   (datetime<? (date-range-start-date new-dr) (date-range-start-date current-dr))
   (datetime>? (date-range-end-date new-dr) (date-range-start-date current-dr))))

(define (split new-dr current-dr)
  (let ([current-dr-value (date-range-value current-dr)])
    (list
     (date-range (date-range-start-date current-dr) (date-range-start-date new-dr) current-dr-value)
     new-dr
     (date-range (date-range-end-date new-dr) (date-range-end-date current-dr) current-dr-value))))

(define (overlap new-dr current-dr)
  ;;do the date ranges touch in any direction
  (cond
   [(contained? current-dr new-dr) new-dr]
   [(contained? new-dr current-dr) (split new-dr current-dr)]
   [(identical? new-dr current-dr) new-dr]
   [(overlap-after-current? new-dr current-dr) (list (new-date-range new-dr current-dr 'end) new-dr)]
   [(overlap-before-current? new-dr current-dr) (list new-dr (new-date-range new-dr current-dr 'begin))]
   [else #f]))

(define (get-new-date-ranges new-dr drs)
  (if (empty? drs)
      (list new-dr)
      (flatten (map (lambda (dr) (overlap new-dr dr)) drs))))

(define (temporal-create-db)
  (make-hash))

(define (temporal-get db key [lookup-date (now)] [default-value ""])
  (let ([dates (hash-ref db key)])
    (let ([found-block (filter (lambda (dr) (in-range? lookup-date dr)) dates)])
      (if (empty? found-block)
	  default-value
	  (date-range-value (first found-block))))))

(define (temporal-set! db key d1 d2 value)
  (let ([new-dr (date-range d1 d2 value)])
    (hash-set! db key (get-new-date-ranges new-dr (hash-ref db key '())))))


(provide temporal-create-db
	 temporal-get
	 temporal-set!)









