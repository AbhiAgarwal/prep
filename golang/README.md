- Goroutines are lightweight threads (managed by Go, not OS threads).
- go f(a, b) starts a new goroutine which runs f (given f is a function).
- There is no subclassing in Go. Instead, there is interface and struct embedding.
- A receive from a closed channel returns the zero value immediately:

```go
var c = make(chan int, 2)
c <- 1
c <- 2
close(c)
for i := 0; i < 3; i++ {
    fmt.Printf("%d ", <-c) 
}
// 1 2 0
```