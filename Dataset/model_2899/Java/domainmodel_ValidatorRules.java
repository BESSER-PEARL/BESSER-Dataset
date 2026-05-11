





import java.util.List;
import java.util.ArrayList;

public class domainmodel_ValidatorRules  {






    private domainmodel_ValidatorFeature domainmodel_validatorfeature;




    private List<domainmodel_ValidatorRule> domainmodel_validatorrules;


    public domainmodel_ValidatorRules(
    ) {
        this.domainmodel_validatorrules = new ArrayList<>();
    }

    public domainmodel_ValidatorRules(
        ArrayList<domainmodel_ValidatorRule> domainmodel_validatorrules    ) {
        this.domainmodel_validatorrules = domainmodel_validatorrules;
    }


    public domainmodel_ValidatorFeature getDomainmodel_validatorfeature() {
        return domainmodel_validatorfeature;
    }

    public void setDomainmodel_validatorfeature(domainmodel_ValidatorFeature domainmodel_validatorfeature) {
        this.domainmodel_validatorfeature = domainmodel_validatorfeature;
    }
    public List<domainmodel_ValidatorRule> getDomainmodel_validatorrules() {
        return domainmodel_validatorrules;
    }

    public void addDomainmodel_validatorrule(Domainmodel_validatorrule domainmodel_validatorrule) {
        this.domainmodel_validatorrules.add(domainmodel_validatorrule);
    }

}