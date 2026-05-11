





import java.util.List;
import java.util.ArrayList;

public class test_ast_AbstractD  {

    private String derivedString;





    private A a;


    public test_ast_AbstractD(
        String derivedString    ) {
        this.derivedString = derivedString;
    }


    public String getDerivedstring() {
        return derivedString;
    }

    public void setDerivedstring(String derivedString) {
        this.derivedString = derivedString;
    }

    public A getA() {
        return a;
    }

    public void setA(A a) {
        this.a = a;
    }

}