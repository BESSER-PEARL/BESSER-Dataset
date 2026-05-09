





import java.util.List;
import java.util.ArrayList;

public class uma_ContentDescription extends MethodUnit {

    private String externalId;
    private String keyConsiderations;
    private String longPresentationName;
    private String mainDescription;





    private uma_DescribableElement uma_describableelement;




    private List<uma_Section> uma_sections;


    public uma_ContentDescription(
        String externalId,        String keyConsiderations,        String longPresentationName,        String mainDescription    ) {
        super(
        );
        this.externalId = externalId;
        this.keyConsiderations = keyConsiderations;
        this.longPresentationName = longPresentationName;
        this.mainDescription = mainDescription;
        this.uma_sections = new ArrayList<>();
    }

    public uma_ContentDescription(
        String externalId,        String keyConsiderations,        String longPresentationName,        String mainDescription        ArrayList<uma_Section> uma_sections    ) {
        this.externalId = externalId;
        this.keyConsiderations = keyConsiderations;
        this.longPresentationName = longPresentationName;
        this.mainDescription = mainDescription;
        this.uma_sections = uma_sections;
    }

    public String getExternalid() {
        return externalId;
    }

    public void setExternalid(String externalId) {
        this.externalId = externalId;
    }
    public String getKeyconsiderations() {
        return keyConsiderations;
    }

    public void setKeyconsiderations(String keyConsiderations) {
        this.keyConsiderations = keyConsiderations;
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
    public List<uma_Section> getUma_sections() {
        return uma_sections;
    }

    public void addUma_section(Uma_section uma_section) {
        this.uma_sections.add(uma_section);
    }

}