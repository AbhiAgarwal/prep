/*
    - A defer statement pushes a function call onto a list. The list of saved calls is executed after the surrounding function returns. Defer is commonly used to simplify functions that perform various clean-up actions.

    1. A deferred function's arguments are evaluated when the defer statement is evaluated
    2. Deferred function calls are executed in Last In First Out order after_the surrounding function returns.
    3. Deferred functions may read and assign to the returning function's named return values.

    - Panic: a built-in function that stops the ordinary flow of control and begins panicking
    - Recover: a built-in function that regains control of a panicking goroutine.
*/

// Defer
// Other uses of defer (beyond the file.Close example given earlier) include releasing a mutex.
/*
    mu.Lock()
    defer mu.Unlock()
*/

func CopyFile(dstName, srcName string) (written int64, err error) {
    src, err := os.Open(srcName)
    if err != nil {
        return
    }
    defer src.Close()

    dst, err := os.Create(dstName)
    if err != nil {
        return
    }
    defer dst.Close()

    return io.Copy(dst, src)
}

// Panic

func g(i int) {
    if i > 3 {
        fmt.Println("Panicking!")
        panic(fmt.Sprintf("%v", i))
    }
    defer fmt.Println("Defer in g", i)
    fmt.Println("Printing in g", i)
    g(i + 1)
}

