





import java.util.List;
import java.util.ArrayList;

public class iso20022_MessageDefinitionIdentifier extends ModelEntity {

    private String flavour;
    private String businessArea;
    private String messageFunctionality;
    private String version;



    public iso20022_MessageDefinitionIdentifier(
        String flavour,        String businessArea,        String messageFunctionality,        String version    ) {
        super(
        );
        this.flavour = flavour;
        this.businessArea = businessArea;
        this.messageFunctionality = messageFunctionality;
        this.version = version;
    }


    public String getFlavour() {
        return flavour;
    }

    public void setFlavour(String flavour) {
        this.flavour = flavour;
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
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


}