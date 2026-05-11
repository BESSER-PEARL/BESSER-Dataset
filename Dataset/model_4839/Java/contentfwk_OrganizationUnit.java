





import java.util.List;
import java.util.ArrayList;

public class contentfwk_OrganizationUnit extends Element {

    private String headcount;





    private contentfwk_Driver contentfwk_driver;




    private List<contentfwk_Process> contentfwk_processs;




    private List<contentfwk_Driver> contentfwk_drivers;




    private List<contentfwk_Service> contentfwk_services;




    private contentfwk_Service contentfwk_service;




    private contentfwk_Process contentfwk_process;




    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;




    private List<contentfwk_Function> contentfwk_functions;




    private contentfwk_Function contentfwk_function;


    public contentfwk_OrganizationUnit(
        String headcount    ) {
        super(
        );
        this.headcount = headcount;
        this.contentfwk_processs = new ArrayList<>();
        this.contentfwk_drivers = new ArrayList<>();
        this.contentfwk_services = new ArrayList<>();
        this.contentfwk_functions = new ArrayList<>();
    }

    public contentfwk_OrganizationUnit(
        String headcount        ArrayList<contentfwk_Process> contentfwk_processs,        ArrayList<contentfwk_Driver> contentfwk_drivers,        ArrayList<contentfwk_Service> contentfwk_services,        ArrayList<contentfwk_Function> contentfwk_functions    ) {
        this.headcount = headcount;
        this.contentfwk_processs = contentfwk_processs;
        this.contentfwk_drivers = contentfwk_drivers;
        this.contentfwk_services = contentfwk_services;
        this.contentfwk_functions = contentfwk_functions;
    }

    public String getHeadcount() {
        return headcount;
    }

    public void setHeadcount(String headcount) {
        this.headcount = headcount;
    }

    public contentfwk_Driver getContentfwk_driver() {
        return contentfwk_driver;
    }

    public void setContentfwk_driver(contentfwk_Driver contentfwk_driver) {
        this.contentfwk_driver = contentfwk_driver;
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
    public List<contentfwk_Service> getContentfwk_services() {
        return contentfwk_services;
    }

    public void addContentfwk_service(Contentfwk_service contentfwk_service) {
        this.contentfwk_services.add(contentfwk_service);
    }
    public contentfwk_Service getContentfwk_service() {
        return contentfwk_service;
    }

    public void setContentfwk_service(contentfwk_Service contentfwk_service) {
        this.contentfwk_service = contentfwk_service;
    }
    public contentfwk_Process getContentfwk_process() {
        return contentfwk_process;
    }

    public void setContentfwk_process(contentfwk_Process contentfwk_process) {
        this.contentfwk_process = contentfwk_process;
    }
    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }
    public List<contentfwk_Function> getContentfwk_functions() {
        return contentfwk_functions;
    }

    public void addContentfwk_function(Contentfwk_function contentfwk_function) {
        this.contentfwk_functions.add(contentfwk_function);
    }
    public contentfwk_Function getContentfwk_function() {
        return contentfwk_function;
    }

    public void setContentfwk_function(contentfwk_Function contentfwk_function) {
        this.contentfwk_function = contentfwk_function;
    }

}