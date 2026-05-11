





import java.util.List;
import java.util.ArrayList;

public class Etunit_ErrorType  {

    private String expected;
    private String mixed;
    private String actual;



    public Etunit_ErrorType(
        String expected,        String mixed,        String actual    ) {
        this.expected = expected;
        this.mixed = mixed;
        this.actual = actual;
    }


    public String getExpected() {
        return expected;
    }

    public void setExpected(String expected) {
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


}