





import java.util.List;
import java.util.ArrayList;

public class iso20022_MessageDefinitionIdentifier extends ModelEntity {

    private String version;
    private String businessArea;
    private String messageFunctionality;
    private String flavour;



    public iso20022_MessageDefinitionIdentifier(
        String version,        String businessArea,        String messageFunctionality,        String flavour    ) {
        super(
        );
        this.version = version;
        this.businessArea = businessArea;
        this.messageFunctionality = messageFunctionality;
        this.flavour = flavour;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getBusinessarea() {
        return businessArea;
    }

    public void setBusinessarea(String businessArea) {
        this.businessArea = businessArea;
    }
    public String getMessagefunctionality() {
        return messageFunctionality;
    }

    public void setMessagefunctionality(String messageFunctionality) {
        this.messageFunctionality = messageFunctionality;
    }
    public String getFlavour() {
        return flavour;
    }

    public void setFlavour(String flavour) {
        this.flavour = flavour;
    }


}