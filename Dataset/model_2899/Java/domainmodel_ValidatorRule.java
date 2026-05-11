





import java.util.List;
import java.util.ArrayList;

public class domainmodel_ValidatorRule  {

    private String stringRule;





    private domainmodel_ValidatorFeature domainmodel_validatorfeature;


    public domainmodel_ValidatorRule(
        String stringRule    ) {
        this.stringRule = stringRule;
    }


    public String getStringrule() {
        return stringRule;
    }

    public void setStringrule(String stringRule) {
        this.stringRule = stringRule;
    }

    public domainmodel_ValidatorFeature getDomainmodel_validatorfeature() {
        return domainmodel_validatorfeature;
    }

    public void setDomainmodel_validatorfeature(domainmodel_ValidatorFeature domainmodel_validatorfeature) {
        this.domainmodel_validatorfeature = domainmodel_validatorfeature;
    }

}