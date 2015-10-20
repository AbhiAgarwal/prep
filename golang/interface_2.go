var val interface{}
val = "foo"
if str, ok := val.(string); ok {
    fmt.Println(str)
}