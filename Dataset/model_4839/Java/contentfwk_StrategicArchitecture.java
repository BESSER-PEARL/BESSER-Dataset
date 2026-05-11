





import java.util.List;
import java.util.ArrayList;

public class contentfwk_StrategicArchitecture extends Architecture {






    private List<contentfwk_StrategicElement> contentfwk_strategicelements;




    private List<contentfwk_Capability> contentfwk_capabilitys;


    public contentfwk_StrategicArchitecture(
    ) {
        super(
        );
        this.contentfwk_strategicelements = new ArrayList<>();
        this.contentfwk_capabilitys = new ArrayList<>();
    }

    public contentfwk_StrategicArchitecture(
        ArrayList<contentfwk_StrategicElement> contentfwk_strategicelements,        ArrayList<contentfwk_Capability> contentfwk_capabilitys    ) {
        this.contentfwk_strategicelements = contentfwk_strategicelements;
        this.contentfwk_capabilitys = contentfwk_capabilitys;
    }


    public List<contentfwk_StrategicElement> getContentfwk_strategicelements() {
        return contentfwk_strategicelements;
    }

    public void addContentfwk_strategicelement(Contentfwk_strategicelement contentfwk_strategicelement) {
        this.contentfwk_strategicelements.add(contentfwk_strategicelement);
    }
    public List<contentfwk_Capability> getContentfwk_capabilitys() {
        return contentfwk_capabilitys;
    }

    public void addContentfwk_capability(Contentfwk_capability contentfwk_capability) {
        this.contentfwk_capabilitys.add(contentfwk_capability);
    }

}