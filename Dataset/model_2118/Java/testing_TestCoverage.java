





import java.util.List;
import java.util.ArrayList;

public class testing_TestCoverage  {






    private testing_TestSuite testing_testsuite;




    private List<testing_TestCase> testing_testcases;


    public testing_TestCoverage(
    ) {
        this.testing_testcases = new ArrayList<>();
    }

    public testing_TestCoverage(
        ArrayList<testing_TestCase> testing_testcases    ) {
        this.testing_testcases = testing_testcases;
    }


    public testing_TestSuite getTesting_testsuite() {
        return testing_testsuite;
    }

    public void setTesting_testsuite(testing_TestSuite testing_testsuite) {
        this.testing_testsuite = testing_testsuite;
    }
    public List<testing_TestCase> getTesting_testcases() {
        return testing_testcases;
    }

    public void addTesting_testcase(Testing_testcase testing_testcase) {
        this.testing_testcases.add(testing_testcase);
    }

}