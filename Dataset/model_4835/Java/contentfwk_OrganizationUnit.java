





import java.util.List;
import java.util.ArrayList;

public class contentfwk_OrganizationUnit extends Element {

    private String headcount;





    private List<contentfwk_Function> contentfwk_functions;




    private List<contentfwk_OrganizationUnit> contentfwk_organizationunits;




    private contentfwk_Driver contentfwk_driver;




    private List<contentfwk_Product> contentfwk_products;




    private contentfwk_Product contentfwk_product;




    private contentfwk_Process contentfwk_process;




    private contentfwk_OrganizationUnit contentfwk_organizationunit;




    private contentfwk_Location contentfwk_location;




    private contentfwk_Function contentfwk_function;




    private contentfwk_Location contentfwk_location;




    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;




    private List<contentfwk_Process> contentfwk_processs;




    private List<contentfwk_Driver> contentfwk_drivers;


    public contentfwk_OrganizationUnit(
        String headcount    ) {
        super(
        );
        this.headcount = headcount;
        this.contentfwk_functions = new ArrayList<>();
        this.contentfwk_organizationunits = new ArrayList<>();
        this.contentfwk_products = new ArrayList<>();
        this.contentfwk_processs = new ArrayList<>();
        this.contentfwk_drivers = new ArrayList<>();
    }

    public contentfwk_OrganizationUnit(
        String headcount        ArrayList<contentfwk_Function> contentfwk_functions,        ArrayList<contentfwk_OrganizationUnit> contentfwk_organizationunits,        ArrayList<contentfwk_Product> contentfwk_products,        ArrayList<contentfwk_Process> contentfwk_processs,        ArrayList<contentfwk_Driver> contentfwk_drivers    ) {
        this.headcount = headcount;
        this.contentfwk_functions = contentfwk_functions;
        this.contentfwk_organizationunits = contentfwk_organizationunits;
        this.contentfwk_products = contentfwk_products;
        this.contentfwk_processs = contentfwk_processs;
        this.contentfwk_drivers = contentfwk_drivers;
    }

    public String getHeadcount() {
        return headcount;
    }

    public void setHeadcount(String headcount) {
        this.headcount = headcount;
    }

    public List<contentfwk_Function> getContentfwk_functions() {
        return contentfwk_functions;
    }

    public void addContentfwk_function(Contentfwk_function contentfwk_function) {
        this.contentfwk_functions.add(contentfwk_function);
    }
    public List<contentfwk_OrganizationUnit> getContentfwk_organizationunits() {
        return contentfwk_organizationunits;
    }

    public void addContentfwk_organizationunit(Contentfwk_organizationunit contentfwk_organizationunit) {
        this.contentfwk_organizationunits.add(contentfwk_organizationunit);
    }
    public contentfwk_Driver getContentfwk_driver() {
        return contentfwk_driver;
    }

    public void setContentfwk_driver(contentfwk_Driver contentfwk_driver) {
        this.contentfwk_driver = contentfwk_driver;
    }
    public List<contentfwk_Product> getContentfwk_products() {
        return contentfwk_products;
    }

    public void addContentfwk_product(Contentfwk_product contentfwk_product) {
        this.contentfwk_products.add(contentfwk_product);
    }
    public contentfwk_Product getContentfwk_product() {
        return contentfwk_product;
    }

    public void setContentfwk_product(contentfwk_Product contentfwk_product) {
        this.contentfwk_product = contentfwk_product;
    }
    public contentfwk_Process getContentfwk_process() {
        return contentfwk_process;
    }

    public void setContentfwk_process(contentfwk_Process contentfwk_process) {
        this.contentfwk_process = contentfwk_process;
    }
    public contentfwk_OrganizationUnit getContentfwk_organizationunit() {
        return contentfwk_organizationunit;
    }

    public void setContentfwk_organizationunit(contentfwk_OrganizationUnit contentfwk_organizationunit) {
        this.contentfwk_organizationunit = contentfwk_organizationunit;
    }
    public contentfwk_Location getContentfwk_location() {
        return contentfwk_location;
    }

    public void setContentfwk_location(contentfwk_Location contentfwk_location) {
        this.contentfwk_location = contentfwk_location;
    }
    public contentfwk_Function getContentfwk_function() {
        return contentfwk_function;
    }

    public void setContentfwk_function(contentfwk_Function contentfwk_function) {
        this.contentfwk_function = contentfwk_function;
    }
    public contentfwk_Location getContentfwk_location() {
        return contentfwk_location;
    }

    public void setContentfwk_location(contentfwk_Location contentfwk_location) {
        this.contentfwk_location = contentfwk_location;
    }
    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }
    public List<contentfwk_Process> getContentfwk_processs() {
        return contentfwk_processs;
    }

    public void addContentfwk_process(Contentfwk_process contentfwk_process) {
        this.contentfwk_processs.add(contentfwk_process);
    }
    public List<contentfwk_Driver> getContentfwk_drivers() {
        return contentfwk_drivers;
    }

    public void addContentfwk_driver(Contentfwk_driver contentfwk_driver) {
        this.contentfwk_drivers.add(contentfwk_driver);
    }

}