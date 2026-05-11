





import java.util.List;
import java.util.ArrayList;

public class model_ComparisonProblem extends TestProblem {

    private String expected;
    private String actual;



    public model_ComparisonProblem(
        String expected,        String actual    ) {
        super(
        );
        this.expected = expected;
        this.actual = actual;
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