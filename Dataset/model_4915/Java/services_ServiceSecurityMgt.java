





import java.util.List;
import java.util.ArrayList;

public class services_ServiceSecurityMgt  {

    private String securityRating;
    private String drRecoveryPlan;
    private String drPlanContact;
    private String drPlanRepository;



    public services_ServiceSecurityMgt(
        String securityRating,        String drRecoveryPlan,        String drPlanContact,        String drPlanRepository    ) {
        this.securityRating = securityRating;
        this.drRecoveryPlan = drRecoveryPlan;
        this.drPlanContact = drPlanContact;
        this.drPlanRepository = drPlanRepository;
    }


    public String getSecurityrating() {
        return securityRating;
    }

    public void setSecurityrating(String securityRating) {
        this.securityRating = securityRating;
    }
    public String getDrrecoveryplan() {
        return drRecoveryPlan;
    }

    public void setDrrecoveryplan(String drRecoveryPlan) {
        this.drRecoveryPlan = drRecoveryPlan;
    }
    public String getDrplancontact() {
        return drPlanContact;
    }

    public void setDrplancontact(String drPlanContact) {
        this.drPlanContact = drPlanContact;
    }
    public String getDrplanrepository() {
        return drPlanRepository;
    }

    public void setDrplanrepository(String drPlanRepository) {
        this.drPlanRepository = drPlanRepository;
    }


}