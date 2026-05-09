





import java.util.List;
import java.util.ArrayList;

public class uma_ContentDescription extends MethodUnit {

    private String keyConsiderations;
    private String externalId;
    private String longPresentationName;
    private String mainDescription;





    private uma_DescribableElement uma_describableelement;


    public uma_ContentDescription(
        String keyConsiderations,        String externalId,        String longPresentationName,        String mainDescription    ) {
        super(
        );
        this.keyConsiderations = keyConsiderations;
        this.externalId = externalId;
        this.longPresentationName = longPresentationName;
        this.mainDescription = mainDescription;
    }


    public String getKeyconsiderations() {
        return keyConsiderations;
    }

    public void setKeyconsiderations(String keyConsiderations) {
        this.keyConsiderations = keyConsiderations;
    }
    public String getExternalid() {
        return externalId;
    }

    public void setExternalid(String externalId) {
        this.externalId = externalId;
    }
    public String getLongpresentationname() {
        return longPresentationName;
    }

    public void setLongpresentationname(String longPresentationName) {
        this.longPresentationName = longPresentationName;
    }
    public String getMaindescription() {
        return mainDescription;
    }

    public void setMaindescription(String mainDescription) {
        this.mainDescription = mainDescription;
    }

    public uma_DescribableElement getUma_describableelement() {
        return uma_describableelement;
    }

    public void setUma_describableelement(uma_DescribableElement uma_describableelement) {
        this.uma_describableelement = uma_describableelement;
    }

}