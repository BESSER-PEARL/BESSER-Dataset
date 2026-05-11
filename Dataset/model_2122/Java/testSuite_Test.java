





import java.util.List;
import java.util.ArrayList;

public class testSuite_Test  {

    private String name;





    private testSuite_Model testsuite_model;


    public testSuite_Test(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public testSuite_Model getTestsuite_model() {
        return testsuite_model;
    }

    public void setTestsuite_model(testSuite_Model testsuite_model) {
        this.testsuite_model = testsuite_model;
    }

}