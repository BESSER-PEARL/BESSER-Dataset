





import java.util.List;
import java.util.ArrayList;

public class test_Bar  {

    private String barA;





    private test_Container test_container;




    private test_Foo test_foo;


    public test_Bar(
        String barA    ) {
        this.barA = barA;
    }


    public String getBara() {
        return barA;
    }

    public void setBara(String barA) {
        this.barA = barA;
    }

    public test_Container getTest_container() {
        return test_container;
    }

    public void setTest_container(test_Container test_container) {
        this.test_container = test_container;
    }
    public test_Foo getTest_foo() {
        return test_foo;
    }

    public void setTest_foo(test_Foo test_foo) {
        this.test_foo = test_foo;
    }

}