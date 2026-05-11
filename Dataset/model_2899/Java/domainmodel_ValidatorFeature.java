





import java.util.List;
import java.util.ArrayList;

public class domainmodel_ValidatorFeature  {

    private String name;





    private domainmodel_ValidatorModule domainmodel_validatormodule;




    private domainmodel_ValidateAction domainmodel_validateaction;


    public domainmodel_ValidatorFeature(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public domainmodel_ValidatorModule getDomainmodel_validatormodule() {
        return domainmodel_validatormodule;
    }

    public void setDomainmodel_validatormodule(domainmodel_ValidatorModule domainmodel_validatormodule) {
        this.domainmodel_validatormodule = domainmodel_validatormodule;
    }
    public domainmodel_ValidateAction getDomainmodel_validateaction() {
        return domainmodel_validateaction;
    }

    public void setDomainmodel_validateaction(domainmodel_ValidateAction domainmodel_validateaction) {
        this.domainmodel_validateaction = domainmodel_validateaction;
    }

}