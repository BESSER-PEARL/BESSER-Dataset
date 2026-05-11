





import java.util.List;
import java.util.ArrayList;

public class Etunit_FailureType  {

    private String mixed;
    private String actual;
    private String expected;



    public Etunit_FailureType(
        String mixed,        String actual,        String expected    ) {
        this.mixed = mixed;
        this.actual = actual;
        this.expected = expected;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getActual() {
        return actual;
    }

    public void setActual(String actual) {
        this.actual = actual;
    }
    public String getExpected() {
        return expected;
    }

    public void setExpected(String expected) {
        this.expected = expected;
    }


}