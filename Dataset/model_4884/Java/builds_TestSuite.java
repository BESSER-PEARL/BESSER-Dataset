





import java.util.List;
import java.util.ArrayList;

public class builds_TestSuite extends TestElement {






    private builds_TestResult builds_testresult;




    private builds_TestCase builds_testcase;




    private List<builds_TestCase> builds_testcases;




    private builds_TestResult builds_testresult;


    public builds_TestSuite(
    ) {
        super(
        );
        this.builds_testcases = new ArrayList<>();
    }

    public builds_TestSuite(
        ArrayList<builds_TestCase> builds_testcases    ) {
        this.builds_testcases = builds_testcases;
    }


    public builds_TestResult getBuilds_testresult() {
        return builds_testresult;
    }

    public void setBuilds_testresult(builds_TestResult builds_testresult) {
        this.builds_testresult = builds_testresult;
    }
    public builds_TestCase getBuilds_testcase() {
        return builds_testcase;
    }

    public void setBuilds_testcase(builds_TestCase builds_testcase) {
        this.builds_testcase = builds_testcase;
    }
    public List<builds_TestCase> getBuilds_testcases() {
        return builds_testcases;
    }

    public void addBuilds_testcase(Builds_testcase builds_testcase) {
        this.builds_testcases.add(builds_testcase);
    }
    public builds_TestResult getBuilds_testresult() {
        return builds_testresult;
    }

    public void setBuilds_testresult(builds_TestResult builds_testresult) {
        this.builds_testresult = builds_testresult;
    }

}