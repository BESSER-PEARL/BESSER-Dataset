





import java.util.List;
import java.util.ArrayList;

public class assessment_Entitlements  {






    private assessment_Entitlement assessment_entitlement;




    private List<assessment_Entitlement> assessment_entitlements;




    private assessment_Application assessment_application;




    private assessment_Application assessment_application;


    public assessment_Entitlements(
    ) {
        this.assessment_entitlements = new ArrayList<>();
    }

    public assessment_Entitlements(
        ArrayList<assessment_Entitlement> assessment_entitlements    ) {
        this.assessment_entitlements = assessment_entitlements;
    }


    public assessment_Entitlement getAssessment_entitlement() {
        return assessment_entitlement;
    }

    public void setAssessment_entitlement(assessment_Entitlement assessment_entitlement) {
        this.assessment_entitlement = assessment_entitlement;
    }
    public List<assessment_Entitlement> getAssessment_entitlements() {
        return assessment_entitlements;
    }

    public void addAssessment_entitlement(Assessment_entitlement assessment_entitlement) {
        this.assessment_entitlements.add(assessment_entitlement);
    }
    public assessment_Application getAssessment_application() {
        return assessment_application;
    }

    public void setAssessment_application(assessment_Application assessment_application) {
        this.assessment_application = assessment_application;
    }
    public assessment_Application getAssessment_application() {
        return assessment_application;
    }

    public void setAssessment_application(assessment_Application assessment_application) {
        this.assessment_application = assessment_application;
    }

}