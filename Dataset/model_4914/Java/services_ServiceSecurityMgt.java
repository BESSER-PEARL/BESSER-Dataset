





import java.util.List;
import java.util.ArrayList;

public class services_ServiceSecurityMgt  {

    private String securityRating;
    private String drRecoveryPlan;
    private String drPlanRepository;
    private String drPlanContact;





    private services_Service services_service;


    public services_ServiceSecurityMgt(
        String securityRating,        String drRecoveryPlan,        String drPlanRepository,        String drPlanContact    ) {
        this.securityRating = securityRating;
        this.drRecoveryPlan = drRecoveryPlan;
        this.drPlanRepository = drPlanRepository;
        this.drPlanContact = drPlanContact;
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
    public String getDrplanrepository() {
        return drPlanRepository;
    }

    public void setDrplanrepository(String drPlanRepository) {
        this.drPlanRepository = drPlanRepository;
    }
    public String getDrplancontact() {
        return drPlanContact;
    }

    public void setDrplancontact(String drPlanContact) {
        this.drPlanContact = drPlanContact;
    }

    public services_Service getServices_service() {
        return services_service;
    }

    public void setServices_service(services_Service services_service) {
        this.services_service = services_service;
    }

}