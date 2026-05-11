





import java.util.List;
import java.util.ArrayList;

public class Etunit_FailureType  {

    private String expected;
    private String actual;
    private String mixed;



    public Etunit_FailureType(
        String expected,        String actual,        String mixed    ) {
        this.expected = expected;
        this.actual = actual;
        this.mixed = mixed;
    }


    public String getExpected() {
        return expected;
    }

    public void setExpected(String expected) {
        this.expected = expected;
    }
    public String getActual() {
        return actual;
    }

    public void setActual(String actual) {
        this.actual = actual;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }


}