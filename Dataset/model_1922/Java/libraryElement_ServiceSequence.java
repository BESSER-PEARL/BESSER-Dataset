





import java.util.List;
import java.util.ArrayList;

public class libraryElement_ServiceSequence extends INamedElement {

    private String TestResult;



    public libraryElement_ServiceSequence(
        String TestResult    ) {
        super(
        );
        this.TestResult = TestResult;
    }


    public String getTestresult() {
        return TestResult;
    }

    public void setTestresult(String TestResult) {
        this.TestResult = TestResult;
    }


}