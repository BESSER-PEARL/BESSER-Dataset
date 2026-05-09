





import java.util.List;
import java.util.ArrayList;

public class uma_ContentDescription extends MethodUnit {

    private String mainDescription;
    private String keyConsiderations;
    private String externalId;





    private List<uma_Section> uma_sections;




    private uma_DescribableElement uma_describableelement;


    public uma_ContentDescription(
        String mainDescription,        String keyConsiderations,        String externalId    ) {
        super(
        );
        this.mainDescription = mainDescription;
        this.keyConsiderations = keyConsiderations;
        this.externalId = externalId;
        this.uma_sections = new ArrayList<>();
    }

    public uma_ContentDescription(
        String mainDescription,        String keyConsiderations,        String externalId        ArrayList<uma_Section> uma_sections    ) {
        this.mainDescription = mainDescription;
        this.keyConsiderations = keyConsiderations;
        this.externalId = externalId;
        this.uma_sections = uma_sections;
    }

    public String getMaindescription() {
        return mainDescription;
    }

    public void setMaindescription(String mainDescription) {
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

    public List<uma_Section> getUma_sections() {
        return uma_sections;
    }

    public void addUma_section(Uma_section uma_section) {
        this.uma_sections.add(uma_section);
    }
    public uma_DescribableElement getUma_describableelement() {
        return uma_describableelement;
    }

    public void setUma_describableelement(uma_DescribableElement uma_describableelement) {
        this.uma_describableelement = uma_describableelement;
    }

}