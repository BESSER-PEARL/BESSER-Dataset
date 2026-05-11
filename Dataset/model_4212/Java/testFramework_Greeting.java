





import java.util.List;
import java.util.ArrayList;

public class testFramework_Greeting  {

    private String summaryDetails;
    private int testcaseValue;





    private testFramework_Model testframework_model;


    public testFramework_Greeting(
        String summaryDetails,        int testcaseValue    ) {
        this.summaryDetails = summaryDetails;
        this.testcaseValue = testcaseValue;
    }


    public String getSummarydetails() {
        return summaryDetails;
    }

    public void setSummarydetails(String summaryDetails) {
        this.summaryDetails = summaryDetails;
    }
    public int getTestcasevalue() {
        return testcaseValue;
    }

    public void setTestcasevalue(int testcaseValue) {
        this.testcaseValue = testcaseValue;
    }

    public testFramework_Model getTestframework_model() {
        return testframework_model;
    }

    public void setTestframework_model(testFramework_Model testframework_model) {
        this.testframework_model = testframework_model;
    }

}