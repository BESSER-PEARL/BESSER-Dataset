





import java.util.List;
import java.util.ArrayList;

public class Etunit_ErrorType  {

    private String mixed;
    private String expected;
    private String actual;



    public Etunit_ErrorType(
        String mixed,        String expected,        String actual    ) {
        this.mixed = mixed;
        this.expected = expected;
        this.actual = actual;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
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


}