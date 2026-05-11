





import java.util.List;
import java.util.ArrayList;

public class contentfwk_BusinessArchitecture extends Architecture {






    private List<contentfwk_Event> contentfwk_events;




    private List<contentfwk_Process> contentfwk_processs;




    private List<contentfwk_ServiceQuality> contentfwk_servicequalitys;




    private List<contentfwk_BusinessService> contentfwk_businessservices;




    private List<contentfwk_Contract> contentfwk_contracts;




    private List<contentfwk_Location> contentfwk_locations;




    private List<contentfwk_Measure> contentfwk_measures;




    private List<contentfwk_Control> contentfwk_controls;




    private List<contentfwk_Product> contentfwk_products;


    public contentfwk_BusinessArchitecture(
    ) {
        super(
        );
        this.contentfwk_events = new ArrayList<>();
        this.contentfwk_processs = new ArrayList<>();
        this.contentfwk_servicequalitys = new ArrayList<>();
        this.contentfwk_businessservices = new ArrayList<>();
        this.contentfwk_contracts = new ArrayList<>();
        this.contentfwk_locations = new ArrayList<>();
        this.contentfwk_measures = new ArrayList<>();
        this.contentfwk_controls = new ArrayList<>();
        this.contentfwk_products = new ArrayList<>();
    }

    public contentfwk_BusinessArchitecture(
        ArrayList<contentfwk_Event> contentfwk_events,        ArrayList<contentfwk_Process> contentfwk_processs,        ArrayList<contentfwk_ServiceQuality> contentfwk_servicequalitys,        ArrayList<contentfwk_BusinessService> contentfwk_businessservices,        ArrayList<contentfwk_Contract> contentfwk_contracts,        ArrayList<contentfwk_Location> contentfwk_locations,        ArrayList<contentfwk_Measure> contentfwk_measures,        ArrayList<contentfwk_Control> contentfwk_controls,        ArrayList<contentfwk_Product> contentfwk_products    ) {
        this.contentfwk_events = contentfwk_events;
        this.contentfwk_processs = contentfwk_processs;
        this.contentfwk_servicequalitys = contentfwk_servicequalitys;
        this.contentfwk_businessservices = contentfwk_businessservices;
        this.contentfwk_contracts = contentfwk_contracts;
        this.contentfwk_locations = contentfwk_locations;
        this.contentfwk_measures = contentfwk_measures;
        this.contentfwk_controls = contentfwk_controls;
        this.contentfwk_products = contentfwk_products;
    }


    public List<contentfwk_Event> getContentfwk_events() {
        return contentfwk_events;
    }

    public void addContentfwk_event(Contentfwk_event contentfwk_event) {
        this.contentfwk_events.add(contentfwk_event);
    }
    public List<contentfwk_Process> getContentfwk_processs() {
        return contentfwk_processs;
    }

    public void addContentfwk_process(Contentfwk_process contentfwk_process) {
        this.contentfwk_processs.add(contentfwk_process);
    }
    public List<contentfwk_ServiceQuality> getContentfwk_servicequalitys() {
        return contentfwk_servicequalitys;
    }

    public void addContentfwk_servicequality(Contentfwk_servicequality contentfwk_servicequality) {
        this.contentfwk_servicequalitys.add(contentfwk_servicequality);
    }
    public List<contentfwk_BusinessService> getContentfwk_businessservices() {
        return contentfwk_businessservices;
    }

    public void addContentfwk_businessservice(Contentfwk_businessservice contentfwk_businessservice) {
        this.contentfwk_businessservices.add(contentfwk_businessservice);
    }
    public List<contentfwk_Contract> getContentfwk_contracts() {
        return contentfwk_contracts;
    }

    public void addContentfwk_contract(Contentfwk_contract contentfwk_contract) {
        this.contentfwk_contracts.add(contentfwk_contract);
    }
    public List<contentfwk_Location> getContentfwk_locations() {
        return contentfwk_locations;
    }

    public void addContentfwk_location(Contentfwk_location contentfwk_location) {
        this.contentfwk_locations.add(contentfwk_location);
    }
    public List<contentfwk_Measure> getContentfwk_measures() {
        return contentfwk_measures;
    }

    public void addContentfwk_measure(Contentfwk_measure contentfwk_measure) {
        this.contentfwk_measures.add(contentfwk_measure);
    }
    public List<contentfwk_Control> getContentfwk_controls() {
        return contentfwk_controls;
    }

    public void addContentfwk_control(Contentfwk_control contentfwk_control) {
        this.contentfwk_controls.add(contentfwk_control);
    }
    public List<contentfwk_Product> getContentfwk_products() {
        return contentfwk_products;
    }

    public void addContentfwk_product(Contentfwk_product contentfwk_product) {
        this.contentfwk_products.add(contentfwk_product);
    }

}