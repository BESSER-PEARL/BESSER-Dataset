





import java.util.List;
import java.util.ArrayList;

public class contentfwk_ApplicationArchitecture extends Architecture {






    private List<contentfwk_InformationSystemService> contentfwk_informationsystemservices;




    private List<contentfwk_LogicalApplicationComponent> contentfwk_logicalapplicationcomponents;




    private List<contentfwk_PhysicalApplicationComponent> contentfwk_physicalapplicationcomponents;


    public contentfwk_ApplicationArchitecture(
    ) {
        super(
        );
        this.contentfwk_informationsystemservices = new ArrayList<>();
        this.contentfwk_logicalapplicationcomponents = new ArrayList<>();
        this.contentfwk_physicalapplicationcomponents = new ArrayList<>();
    }

    public contentfwk_ApplicationArchitecture(
        ArrayList<contentfwk_InformationSystemService> contentfwk_informationsystemservices,        ArrayList<contentfwk_LogicalApplicationComponent> contentfwk_logicalapplicationcomponents,        ArrayList<contentfwk_PhysicalApplicationComponent> contentfwk_physicalapplicationcomponents    ) {
        this.contentfwk_informationsystemservices = contentfwk_informationsystemservices;
        this.contentfwk_logicalapplicationcomponents = contentfwk_logicalapplicationcomponents;
        this.contentfwk_physicalapplicationcomponents = contentfwk_physicalapplicationcomponents;
    }


    public List<contentfwk_InformationSystemService> getContentfwk_informationsystemservices() {
        return contentfwk_informationsystemservices;
    }

    public void addContentfwk_informationsystemservice(Contentfwk_informationsystemservice contentfwk_informationsystemservice) {
        this.contentfwk_informationsystemservices.add(contentfwk_informationsystemservice);
    }
    public List<contentfwk_LogicalApplicationComponent> getContentfwk_logicalapplicationcomponents() {
        return contentfwk_logicalapplicationcomponents;
    }

    public void addContentfwk_logicalapplicationcomponent(Contentfwk_logicalapplicationcomponent contentfwk_logicalapplicationcomponent) {
        this.contentfwk_logicalapplicationcomponents.add(contentfwk_logicalapplicationcomponent);
    }
    public List<contentfwk_PhysicalApplicationComponent> getContentfwk_physicalapplicationcomponents() {
        return contentfwk_physicalapplicationcomponents;
    }

    public void addContentfwk_physicalapplicationcomponent(Contentfwk_physicalapplicationcomponent contentfwk_physicalapplicationcomponent) {
        this.contentfwk_physicalapplicationcomponents.add(contentfwk_physicalapplicationcomponent);
    }

}