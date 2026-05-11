





import java.util.List;
import java.util.ArrayList;

public class contentfwk_PhysicalTechnologyComponent extends Element, TechnologyComponent {

    private String version;
    private String productName;
    private String moduleName;
    private String vendor;





    private contentfwk_TechnologyArchitecture contentfwk_technologyarchitecture;




    private contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent;




    private contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent;


    public contentfwk_PhysicalTechnologyComponent(
        String version,        String productName,        String moduleName,        String vendor    ) {
        super(
        );
        this.version = version;
        this.productName = productName;
        this.moduleName = moduleName;
        this.vendor = vendor;
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
    public String getModulename() {
        return moduleName;
    }

    public void setModulename(String moduleName) {
        this.moduleName = moduleName;
    }
    public String getVendor() {
        return vendor;
    }

    public void setVendor(String vendor) {
        this.vendor = vendor;
    }

    public contentfwk_TechnologyArchitecture getContentfwk_technologyarchitecture() {
        return contentfwk_technologyarchitecture;
    }

    public void setContentfwk_technologyarchitecture(contentfwk_TechnologyArchitecture contentfwk_technologyarchitecture) {
        this.contentfwk_technologyarchitecture = contentfwk_technologyarchitecture;
    }
    public contentfwk_PhysicalTechnologyComponent getContentfwk_physicaltechnologycomponent() {
        return contentfwk_physicaltechnologycomponent;
    }

    public void setContentfwk_physicaltechnologycomponent(contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent) {
        this.contentfwk_physicaltechnologycomponent = contentfwk_physicaltechnologycomponent;
    }
    public contentfwk_PhysicalTechnologyComponent getContentfwk_physicaltechnologycomponent() {
        return contentfwk_physicaltechnologycomponent;
    }

    public void setContentfwk_physicaltechnologycomponent(contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent) {
        this.contentfwk_physicaltechnologycomponent = contentfwk_physicaltechnologycomponent;
    }

}