





import java.util.List;
import java.util.ArrayList;

public class sipme_Domain extends OrganisationCell, SIPME_object, EnterpriseProcessor {

    private float performanceIndicators;
    private String domainCharacterization;



    public sipme_Domain(
        float performanceIndicators,        String domainCharacterization    ) {
        super(
        );
        this.performanceIndicators = performanceIndicators;
        this.domainCharacterization = domainCharacterization;
    }


    public float getPerformanceindicators() {
        return performanceIndicators;
    }

    public void setPerformanceindicators(float performanceIndicators) {
        this.performanceIndicators = performanceIndicators;
    }
    public String getDomaincharacterization() {
        return domainCharacterization;
    }

    public void setDomaincharacterization(String domainCharacterization) {
        this.domainCharacterization = domainCharacterization;
    }


}