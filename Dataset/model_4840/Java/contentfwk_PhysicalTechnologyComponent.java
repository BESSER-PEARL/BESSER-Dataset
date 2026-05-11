





import java.util.List;
import java.util.ArrayList;

public class contentfwk_PhysicalTechnologyComponent extends TechnologyComponent, Element {

    private String categoryTRM;
    private String productName;
    private String vendor;
    private String moduleName;
    private String version;





    private contentfwk_TechnologyArchitecture contentfwk_technologyarchitecture;




    private List<contentfwk_Location> contentfwk_locations;




    private contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent;




    private contentfwk_Location contentfwk_location;




    private contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent;


    public contentfwk_PhysicalTechnologyComponent(
        String categoryTRM,        String productName,        String vendor,        String moduleName,        String version    ) {
        super(
        );
        this.categoryTRM = categoryTRM;
        this.productName = productName;
        this.vendor = vendor;
        this.moduleName = moduleName;
        this.version = version;
        this.contentfwk_locations = new ArrayList<>();
    }

    public contentfwk_PhysicalTechnologyComponent(
        String categoryTRM,        String productName,        String vendor,        String moduleName,        String version        ArrayList<contentfwk_Location> contentfwk_locations    ) {
        this.categoryTRM = categoryTRM;
        this.productName = productName;
        this.vendor = vendor;
        this.moduleName = moduleName;
        this.version = version;
        this.contentfwk_locations = contentfwk_locations;
    }

    public String getCategorytrm() {
        return categoryTRM;
    }

    public void setCategorytrm(String categoryTRM) {
        this.categoryTRM = categoryTRM;
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
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public contentfwk_TechnologyArchitecture getContentfwk_technologyarchitecture() {
        return contentfwk_technologyarchitecture;
    }

    public void setContentfwk_technologyarchitecture(contentfwk_TechnologyArchitecture contentfwk_technologyarchitecture) {
        this.contentfwk_technologyarchitecture = contentfwk_technologyarchitecture;
    }
    public List<contentfwk_Location> getContentfwk_locations() {
        return contentfwk_locations;
    }

    public void addContentfwk_location(Contentfwk_location contentfwk_location) {
        this.contentfwk_locations.add(contentfwk_location);
    }
    public contentfwk_PhysicalTechnologyComponent getContentfwk_physicaltechnologycomponent() {
        return contentfwk_physicaltechnologycomponent;
    }

    public void setContentfwk_physicaltechnologycomponent(contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent) {
        this.contentfwk_physicaltechnologycomponent = contentfwk_physicaltechnologycomponent;
    }
    public contentfwk_Location getContentfwk_location() {
        return contentfwk_location;
    }

    public void setContentfwk_location(contentfwk_Location contentfwk_location) {
        this.contentfwk_location = contentfwk_location;
    }
    public contentfwk_PhysicalTechnologyComponent getContentfwk_physicaltechnologycomponent() {
        return contentfwk_physicaltechnologycomponent;
    }

    public void setContentfwk_physicaltechnologycomponent(contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent) {
        this.contentfwk_physicaltechnologycomponent = contentfwk_physicaltechnologycomponent;
    }

}