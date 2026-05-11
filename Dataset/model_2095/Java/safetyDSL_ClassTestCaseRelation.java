





import java.util.List;
import java.util.ArrayList;

public class safetyDSL_ClassTestCaseRelation  {

    private String testCases;





    private safetyDSL_ImplementationDetail safetydsl_implementationdetail;


    public safetyDSL_ClassTestCaseRelation(
        String testCases    ) {
        this.testCases = testCases;
    }


    public String getTestcases() {
        return testCases;
    }

    public void setTestcases(String testCases) {
        this.testCases = testCases;
    }

    public safetyDSL_ImplementationDetail getSafetydsl_implementationdetail() {
        return safetydsl_implementationdetail;
    }

    public void setSafetydsl_implementationdetail(safetyDSL_ImplementationDetail safetydsl_implementationdetail) {
        this.safetydsl_implementationdetail = safetydsl_implementationdetail;
    }

}