





import java.util.List;
import java.util.ArrayList;

public class rapidml_ReferenceRealization extends RealizationContainer {

    private String realizationType;
    private boolean multiValued;





    private rapidml_ResourceAPI rapidml_resourceapi;




    private rapidml_ReferenceTreatment rapidml_referencetreatment;




    private rapidml_ResourceDefinition rapidml_resourcedefinition;




    private rapidml_ReferenceTreatment rapidml_referencetreatment;


    public rapidml_ReferenceRealization(
        String realizationType,        boolean multiValued    ) {
        super(
        );
        this.realizationType = realizationType;
        this.multiValued = multiValued;
    }


    public String getRealizationtype() {
        return realizationType;
    }

    public void setRealizationtype(String realizationType) {
        this.realizationType = realizationType;
    }
    public boolean getMultivalued() {
        return multiValued;
    }

    public void setMultivalued(boolean multiValued) {
        this.multiValued = multiValued;
    }

    public rapidml_ResourceAPI getRapidml_resourceapi() {
        return rapidml_resourceapi;
    }

    public void setRapidml_resourceapi(rapidml_ResourceAPI rapidml_resourceapi) {
        this.rapidml_resourceapi = rapidml_resourceapi;
    }
    public rapidml_ReferenceTreatment getRapidml_referencetreatment() {
        return rapidml_referencetreatment;
    }

    public void setRapidml_referencetreatment(rapidml_ReferenceTreatment rapidml_referencetreatment) {
        this.rapidml_referencetreatment = rapidml_referencetreatment;
    }
    public rapidml_ResourceDefinition getRapidml_resourcedefinition() {
        return rapidml_resourcedefinition;
    }

    public void setRapidml_resourcedefinition(rapidml_ResourceDefinition rapidml_resourcedefinition) {
        this.rapidml_resourcedefinition = rapidml_resourcedefinition;
    }
    public rapidml_ReferenceTreatment getRapidml_referencetreatment() {
        return rapidml_referencetreatment;
    }

    public void setRapidml_referencetreatment(rapidml_ReferenceTreatment rapidml_referencetreatment) {
        this.rapidml_referencetreatment = rapidml_referencetreatment;
    }

}