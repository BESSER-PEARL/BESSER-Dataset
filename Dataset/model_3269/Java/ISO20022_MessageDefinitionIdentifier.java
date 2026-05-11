





import java.util.List;
import java.util.ArrayList;

public class ISO20022_MessageDefinitionIdentifier  {

    private String messageFunctionality;
    private String businessArea;
    private String version;
    private String flavour;





    private ISO20022_MessageDefinition iso20022_messagedefinition;


    public ISO20022_MessageDefinitionIdentifier(
        String messageFunctionality,        String businessArea,        String version,        String flavour    ) {
        this.messageFunctionality = messageFunctionality;
        this.businessArea = businessArea;
        this.version = version;
        this.flavour = flavour;
    }


    public String getMessagefunctionality() {
        return messageFunctionality;
    }

    public void setMessagefunctionality(String messageFunctionality) {
        this.messageFunctionality = messageFunctionality;
    }
    public String getBusinessarea() {
        return businessArea;
    }

    public void setBusinessarea(String businessArea) {
        this.businessArea = businessArea;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getFlavour() {
        return flavour;
    }

    public void setFlavour(String flavour) {
        this.flavour = flavour;
    }

    public ISO20022_MessageDefinition getIso20022_messagedefinition() {
        return iso20022_messagedefinition;
    }

    public void setIso20022_messagedefinition(ISO20022_MessageDefinition iso20022_messagedefinition) {
        this.iso20022_messagedefinition = iso20022_messagedefinition;
    }

}