





import java.util.List;
import java.util.ArrayList;

public class uma_ContentDescription extends MethodUnit {

    private String keyConsiderations;
    private String externalId;
    private String mainDescription;





    private uma_DescribableElement uma_describableelement;




    private List<uma_Section> uma_sections;


    public uma_ContentDescription(
        String keyConsiderations,        String externalId,        String mainDescription    ) {
        super(
        );
        this.keyConsiderations = keyConsiderations;
        this.externalId = externalId;
        this.mainDescription = mainDescription;
        this.uma_sections = new ArrayList<>();
    }

    public uma_ContentDescription(
        String keyConsiderations,        String externalId,        String mainDescription        ArrayList<uma_Section> uma_sections    ) {
        this.keyConsiderations = keyConsiderations;
        this.externalId = externalId;
        this.mainDescription = mainDescription;
        this.uma_sections = uma_sections;
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