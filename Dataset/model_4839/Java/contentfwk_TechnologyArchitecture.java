





import java.util.List;
import java.util.ArrayList;

public class contentfwk_TechnologyArchitecture extends Architecture {






    private List<contentfwk_LogicalTechnologyComponent> contentfwk_logicaltechnologycomponents;




    private List<contentfwk_PlatformService> contentfwk_platformservices;




    private List<contentfwk_PhysicalTechnologyComponent> contentfwk_physicaltechnologycomponents;


    public contentfwk_TechnologyArchitecture(
    ) {
        super(
        );
        this.contentfwk_logicaltechnologycomponents = new ArrayList<>();
        this.contentfwk_platformservices = new ArrayList<>();
        this.contentfwk_physicaltechnologycomponents = new ArrayList<>();
    }

    public contentfwk_TechnologyArchitecture(
        ArrayList<contentfwk_LogicalTechnologyComponent> contentfwk_logicaltechnologycomponents,        ArrayList<contentfwk_PlatformService> contentfwk_platformservices,        ArrayList<contentfwk_PhysicalTechnologyComponent> contentfwk_physicaltechnologycomponents    ) {
        this.contentfwk_logicaltechnologycomponents = contentfwk_logicaltechnologycomponents;
        this.contentfwk_platformservices = contentfwk_platformservices;
        this.contentfwk_physicaltechnologycomponents = contentfwk_physicaltechnologycomponents;
    }


    public List<contentfwk_LogicalTechnologyComponent> getContentfwk_logicaltechnologycomponents() {
        return contentfwk_logicaltechnologycomponents;
    }

    public void addContentfwk_logicaltechnologycomponent(Contentfwk_logicaltechnologycomponent contentfwk_logicaltechnologycomponent) {
        this.contentfwk_logicaltechnologycomponents.add(contentfwk_logicaltechnologycomponent);
    }
    public List<contentfwk_PlatformService> getContentfwk_platformservices() {
        return contentfwk_platformservices;
    }

    public void addContentfwk_platformservice(Contentfwk_platformservice contentfwk_platformservice) {
        this.contentfwk_platformservices.add(contentfwk_platformservice);
    }
    public List<contentfwk_PhysicalTechnologyComponent> getContentfwk_physicaltechnologycomponents() {
        return contentfwk_physicaltechnologycomponents;
    }

    public void addContentfwk_physicaltechnologycomponent(Contentfwk_physicaltechnologycomponent contentfwk_physicaltechnologycomponent) {
        this.contentfwk_physicaltechnologycomponents.add(contentfwk_physicaltechnologycomponent);
    }

}