





import java.util.List;
import java.util.ArrayList;

public class model_TestRoot extends TestContainer {

    private String testRunner;



    public model_TestRoot(
        String testRunner    ) {
        super(
        );
        this.testRunner = testRunner;
    }


    public String getTestrunner() {
        return testRunner;
    }

    public void setTestrunner(String testRunner) {
        this.testRunner = testRunner;
    }


}