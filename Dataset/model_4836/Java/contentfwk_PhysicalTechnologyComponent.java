





import java.util.List;
import java.util.ArrayList;

public class contentfwk_PhysicalTechnologyComponent extends Element, TechnologyComponent {

    private String version;
    private String productName;
    private String vendor;
    private String moduleName;





    private contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent;




    private List<contentfwk_Location> contentfwk_locations;




    private List<contentfwk_PhysicalTechnologyComponent> contentfwk_physicaltechnologycomponents;




    private contentfwk_Location contentfwk_location;




    private contentfwk_TechnologyArchitecture contentfwk_technologyarchitecture;


    public contentfwk_PhysicalTechnologyComponent(
        String version,        String productName,        String vendor,        String moduleName    ) {
        super(
        );
        this.version = version;
        this.productName = productName;
        this.vendor = vendor;
        this.moduleName = moduleName;
        this.contentfwk_locations = new ArrayList<>();
        this.contentfwk_physicaltechnologycomponents = new ArrayList<>();
    }

    public contentfwk_PhysicalTechnologyComponent(
        String version,        String productName,        String vendor,        String moduleName        ArrayList<contentfwk_Location> contentfwk_locations,        ArrayList<contentfwk_PhysicalTechnologyComponent> contentfwk_physicaltechnologycomponents    ) {
        this.version = version;
        this.productName = productName;
        this.vendor = vendor;
        this.moduleName = moduleName;
        this.contentfwk_locations = contentfwk_locations;
        this.contentfwk_physicaltechnologycomponents = contentfwk_physicaltechnologycomponents;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getProductname() {
        return productName;
    }

    public void setProductname(String productName) {
        this.productName = productName;
    }
    public String getVendor() {
        return vendor;
    }

    public void setVendor(String vendor) {
        this.vendor = vendor;
    }
    public String getModulename() {
        return moduleName;
    }

    public void setModulename(String moduleName) {
        this.moduleName = moduleName;
    }

    public contentfwk_PhysicalTechnologyComponent getContentfwk_physicaltechnologycomponent() {
        return contentfwk_physicaltechnologycomponent;
    }

    public void setContentfwk_physicaltechnologycomponent(contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent) {
        this.contentfwk_physicaltechnologycomponent = contentfwk_physicaltechnologycomponent;
    }
    public List<contentfwk_Location> getContentfwk_locations() {
        return contentfwk_locations;
    }

    public void addContentfwk_location(Contentfwk_location contentfwk_location) {
        this.contentfwk_locations.add(contentfwk_location);
    }
    public List<contentfwk_PhysicalTechnologyComponent> getContentfwk_physicaltechnologycomponents() {
        return contentfwk_physicaltechnologycomponents;
    }

    public void addContentfwk_physicaltechnologycomponent(Contentfwk_physicaltechnologycomponent contentfwk_physicaltechnologycomponent) {
        this.contentfwk_physicaltechnologycomponents.add(contentfwk_physicaltechnologycomponent);
    }
    public contentfwk_Location getContentfwk_location() {
        return contentfwk_location;
    }

    public void setContentfwk_location(contentfwk_Location contentfwk_location) {
        this.contentfwk_location = contentfwk_location;
    }
    public contentfwk_TechnologyArchitecture getContentfwk_technologyarchitecture() {
        return contentfwk_technologyarchitecture;
    }

    public void setContentfwk_technologyarchitecture(contentfwk_TechnologyArchitecture contentfwk_technologyarchitecture) {
        this.contentfwk_technologyarchitecture = contentfwk_technologyarchitecture;
    }

}