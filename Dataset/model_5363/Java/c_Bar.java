





import java.util.List;
import java.util.ArrayList;

public class c_Bar extends Foo {

    private String value;





    private List<c_Foo> c_foos;




    private c_Foo c_foo;


    public c_Bar(
        String value    ) {
        super(
        );
        this.value = value;
        this.c_foos = new ArrayList<>();
    }

    public c_Bar(
        String value        ArrayList<c_Foo> c_foos    ) {
        this.value = value;
        this.c_foos = c_foos;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public List<c_Foo> getC_foos() {
        return c_foos;
    }

    public void addC_foo(C_foo c_foo) {
        this.c_foos.add(c_foo);
    }
    public c_Foo getC_foo() {
        return c_foo;
    }

    public void setC_foo(c_Foo c_foo) {
        this.c_foo = c_foo;
    }

}