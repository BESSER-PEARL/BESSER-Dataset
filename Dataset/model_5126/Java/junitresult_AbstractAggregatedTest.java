





import java.util.List;
import java.util.ArrayList;

public class junitresult_AbstractAggregatedTest extends JunitResult {

    private int failures;
    private int tests;
    private String name;
    private int errors;





    private List<junitresult_Testsuite> junitresult_testsuites;


    public junitresult_AbstractAggregatedTest(
        int failures,        int tests,        String name,        int errors    ) {
        super(
        );
        this.failures = failures;
        this.tests = tests;
        this.name = name;
        this.errors = errors;
        this.junitresult_testsuites = new ArrayList<>();
    }

    public junitresult_AbstractAggregatedTest(
        int failures,        int tests,        String name,        int errors        ArrayList<junitresult_Testsuite> junitresult_testsuites    ) {
        this.failures = failures;
        this.tests = tests;
        this.name = name;
        this.errors = errors;
        this.junitresult_testsuites = junitresult_testsuites;
    }

    public int getFailures() {
        return failures;
    }

    public void setFailures(int failures) {
        this.failures = failures;
    }
    public int getTests() {
        return tests;
    }

    public void setTests(int tests) {
        this.tests = tests;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getErrors() {
        return errors;
    }

    public void setErrors(int errors) {
        this.errors = errors;
    }

    public List<junitresult_Testsuite> getJunitresult_testsuites() {
        return junitresult_testsuites;
    }

    public void addJunitresult_testsuite(Junitresult_testsuite junitresult_testsuite) {
        this.junitresult_testsuites.add(junitresult_testsuite);
    }

}