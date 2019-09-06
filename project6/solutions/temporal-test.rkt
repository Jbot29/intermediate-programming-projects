#lang racket
 
(require rackunit
	 gregor
	 "temporal.rkt")



(test-case
 "Identical replace"
  (let ([dbc (temporal-create-db)])
    (temporal-set! dbc "case" (datetime 2019 9 1 12)  (datetime 2019 9 30 12) "cvalue")
    (temporal-set! dbc "case" (datetime 2019 9 1 12)  (datetime 2019 9 30 12) "overridevalue")
    (check-eq? "overridevalue" (temporal-get dbc "case" (datetime 2019 9 15 15)))))


(test-case
 "new dr spans old dr"
 (let ([dbc (temporal-create-db)])
   (temporal-set! dbc "case" (datetime 2019 9 1 12)  (datetime 2019 9 30 12) "cvalue")
   (temporal-set! dbc "case" (datetime 2019 8 1 12)  (datetime 2019 10 1 12) "contained")
   (check-eq? 1 (length (hash-ref dbc "case")))))


(test-case
 "new dr splits old block"
 (let ([dbc (temporal-create-db)])
   (temporal-set! dbc "case" (datetime 2019 9 1 12)  (datetime 2019 9 30 12) "split")
   (temporal-set! dbc "case" (datetime 2019 9 8 12)  (datetime 2019 9 10 12) "nonsplit")
    (check-eq? 3 (length (hash-ref dbc "case")))))


;;Case
(test-case
 "Case: the new dr's end overlaps an existing block"
 (let ([db3 (temporal-create-db)])
   (check-pred hash? db3)
   (temporal-set! db3 "case3" (datetime 2019 9 1 12)  (datetime 2019 9 30 12) "case3value")
   (temporal-set! db3 "case3" (datetime 2019 8 1 12) (datetime 2019 9 20 12) "case3new")
   (check-eq? "case3new" (temporal-get db3 "case3" (datetime 2019 9 15 15)))))



