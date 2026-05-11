





import java.util.List;
import java.util.ArrayList;

public class contentfwk_PhysicalTechnologyComponent extends Element, TechnologyComponent {

    private String productName;
    private String vendor;
    private String moduleName;
    private String version;
    private String categoryTRM;





    private contentfwk_LogicalTechnologyComponent contentfwk_logicaltechnologycomponent;




    private List<contentfwk_PhysicalApplicationComponent> contentfwk_physicalapplicationcomponents;




    private List<contentfwk_PhysicalTechnologyComponent> contentfwk_physicaltechnologycomponents;




    private contentfwk_PhysicalApplicationComponent contentfwk_physicalapplicationcomponent;




    private contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent;




    private List<contentfwk_LogicalTechnologyComponent> contentfwk_logicaltechnologycomponents;


    public contentfwk_PhysicalTechnologyComponent(
        String productName,        String vendor,        String moduleName,        String version,        String categoryTRM    ) {
        super(
        );
        this.productName = productName;
        this.vendor = vendor;
        this.moduleName = moduleName;
        this.version = version;
        this.categoryTRM = categoryTRM;
        this.contentfwk_physicalapplicationcomponents = new ArrayList<>();
        this.contentfwk_physicaltechnologycomponents = new ArrayList<>();
        this.contentfwk_logicaltechnologycomponents = new ArrayList<>();
    }

    public contentfwk_PhysicalTechnologyComponent(
        String productName,        String vendor,        String moduleName,        String version,        String categoryTRM        ArrayList<contentfwk_PhysicalApplicationComponent> contentfwk_physicalapplicationcomponents,        ArrayList<contentfwk_PhysicalTechnologyComponent> contentfwk_physicaltechnologycomponents,        ArrayList<contentfwk_LogicalTechnologyComponent> contentfwk_logicaltechnologycomponents    ) {
        this.productName = productName;
        this.vendor = vendor;
        this.moduleName = moduleName;
        this.version = version;
        this.categoryTRM = categoryTRM;
        this.contentfwk_physicalapplicationcomponents = contentfwk_physicalapplicationcomponents;
        this.contentfwk_physicaltechnologycomponents = contentfwk_physicaltechnologycomponents;
        this.contentfwk_logicaltechnologycomponents = contentfwk_logicaltechnologycomponents;
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
    public String getCategorytrm() {
        return categoryTRM;
    }

    public void setCategorytrm(String categoryTRM) {
        this.categoryTRM = categoryTRM;
    }

    public contentfwk_LogicalTechnologyComponent getContentfwk_logicaltechnologycomponent() {
        return contentfwk_logicaltechnologycomponent;
    }

    public void setContentfwk_logicaltechnologycomponent(contentfwk_LogicalTechnologyComponent contentfwk_logicaltechnologycomponent) {
        this.contentfwk_logicaltechnologycomponent = contentfwk_logicaltechnologycomponent;
    }
    public List<contentfwk_PhysicalApplicationComponent> getContentfwk_physicalapplicationcomponents() {
        return contentfwk_physicalapplicationcomponents;
    }

    public void addContentfwk_physicalapplicationcomponent(Contentfwk_physicalapplicationcomponent contentfwk_physicalapplicationcomponent) {
        this.contentfwk_physicalapplicationcomponents.add(contentfwk_physicalapplicationcomponent);
    }
    public List<contentfwk_PhysicalTechnologyComponent> getContentfwk_physicaltechnologycomponents() {
        return contentfwk_physicaltechnologycomponents;
    }

    public void addContentfwk_physicaltechnologycomponent(Contentfwk_physicaltechnologycomponent contentfwk_physicaltechnologycomponent) {
        this.contentfwk_physicaltechnologycomponents.add(contentfwk_physicaltechnologycomponent);
    }
    public contentfwk_PhysicalApplicationComponent getContentfwk_physicalapplicationcomponent() {
        return contentfwk_physicalapplicationcomponent;
    }

    public void setContentfwk_physicalapplicationcomponent(contentfwk_PhysicalApplicationComponent contentfwk_physicalapplicationcomponent) {
        this.contentfwk_physicalapplicationcomponent = contentfwk_physicalapplicationcomponent;
    }
    public contentfwk_PhysicalTechnologyComponent getContentfwk_physicaltechnologycomponent() {
        return contentfwk_physicaltechnologycomponent;
    }

    public void setContentfwk_physicaltechnologycomponent(contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent) {
        this.contentfwk_physicaltechnologycomponent = contentfwk_physicaltechnologycomponent;
    }
    public List<contentfwk_LogicalTechnologyComponent> getContentfwk_logicaltechnologycomponents() {
        return contentfwk_logicaltechnologycomponents;
    }

    public void addContentfwk_logicaltechnologycomponent(Contentfwk_logicaltechnologycomponent contentfwk_logicaltechnologycomponent) {
        this.contentfwk_logicaltechnologycomponents.add(contentfwk_logicaltechnologycomponent);
    }

}