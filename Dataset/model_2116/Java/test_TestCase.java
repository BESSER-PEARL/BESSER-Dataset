





import java.util.List;
import java.util.ArrayList;

public class test_TestCase extends NamedElement {

    private String description;





    private List<test_TestStep> test_teststeps;




    private test_TestSuite test_testsuite;


    public test_TestCase(
        String description    ) {
        super(
        );
        this.description = description;
        this.test_teststeps = new ArrayList<>();
    }

    public test_TestCase(
        String description        ArrayList<test_TestStep> test_teststeps    ) {
        this.description = description;
        this.test_teststeps = test_teststeps;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<test_TestStep> getTest_teststeps() {
        return test_teststeps;
    }

    public void addTest_teststep(Test_teststep test_teststep) {
        this.test_teststeps.add(test_teststep);
    }
    public test_TestSuite getTest_testsuite() {
        return test_testsuite;
    }

    public void setTest_testsuite(test_TestSuite test_testsuite) {
        this.test_testsuite = test_testsuite;
    }

}