





import java.util.List;
import java.util.ArrayList;

public class driver_TestCasesList  {

    private String operator;





    private List<driver_TestCase> driver_testcases;




    private driver_TestExecuteScript driver_testexecutescript;


    public driver_TestCasesList(
        String operator    ) {
        this.operator = operator;
        this.driver_testcases = new ArrayList<>();
    }

    public driver_TestCasesList(
        String operator        ArrayList<driver_TestCase> driver_testcases    ) {
        this.operator = operator;
        this.driver_testcases = driver_testcases;
    }

    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public List<driver_TestCase> getDriver_testcases() {
        return driver_testcases;
    }

    public void addDriver_testcase(Driver_testcase driver_testcase) {
        this.driver_testcases.add(driver_testcase);
    }
    public driver_TestExecuteScript getDriver_testexecutescript() {
        return driver_testexecutescript;
    }

    public void setDriver_testexecutescript(driver_TestExecuteScript driver_testexecutescript) {
        this.driver_testexecutescript = driver_testexecutescript;
    }

}