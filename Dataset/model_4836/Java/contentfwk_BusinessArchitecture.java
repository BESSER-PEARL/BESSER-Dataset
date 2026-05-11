





import java.util.List;
import java.util.ArrayList;

public class contentfwk_BusinessArchitecture extends Architecture {






    private List<contentfwk_Location> contentfwk_locations;




    private List<contentfwk_Process> contentfwk_processs;




    private List<contentfwk_Product> contentfwk_products;




    private List<contentfwk_Event> contentfwk_events;




    private List<contentfwk_Control> contentfwk_controls;




    private List<contentfwk_BusinessService> contentfwk_businessservices;




    private List<contentfwk_Function> contentfwk_functions;


    public contentfwk_BusinessArchitecture(
    ) {
        super(
        );
        this.contentfwk_locations = new ArrayList<>();
        this.contentfwk_processs = new ArrayList<>();
        this.contentfwk_products = new ArrayList<>();
        this.contentfwk_events = new ArrayList<>();
        this.contentfwk_controls = new ArrayList<>();
        this.contentfwk_businessservices = new ArrayList<>();
        this.contentfwk_functions = new ArrayList<>();
    }

    public contentfwk_BusinessArchitecture(
        ArrayList<contentfwk_Location> contentfwk_locations,        ArrayList<contentfwk_Process> contentfwk_processs,        ArrayList<contentfwk_Product> contentfwk_products,        ArrayList<contentfwk_Event> contentfwk_events,        ArrayList<contentfwk_Control> contentfwk_controls,        ArrayList<contentfwk_BusinessService> contentfwk_businessservices,        ArrayList<contentfwk_Function> contentfwk_functions    ) {
        this.contentfwk_locations = contentfwk_locations;
        this.contentfwk_processs = contentfwk_processs;
        this.contentfwk_products = contentfwk_products;
        this.contentfwk_events = contentfwk_events;
        this.contentfwk_controls = contentfwk_controls;
        this.contentfwk_businessservices = contentfwk_businessservices;
        this.contentfwk_functions = contentfwk_functions;
    }


    public List<contentfwk_Location> getContentfwk_locations() {
        return contentfwk_locations;
    }

    public void addContentfwk_location(Contentfwk_location contentfwk_location) {
        this.contentfwk_locations.add(contentfwk_location);
    }
    public List<contentfwk_Process> getContentfwk_processs() {
        return contentfwk_processs;
    }

    public void addContentfwk_process(Contentfwk_process contentfwk_process) {
        this.contentfwk_processs.add(contentfwk_process);
    }
    public List<contentfwk_Product> getContentfwk_products() {
        return contentfwk_products;
    }

    public void addContentfwk_product(Contentfwk_product contentfwk_product) {
        this.contentfwk_products.add(contentfwk_product);
    }
    public List<contentfwk_Event> getContentfwk_events() {
        return contentfwk_events;
    }

    public void addContentfwk_event(Contentfwk_event contentfwk_event) {
        this.contentfwk_events.add(contentfwk_event);
    }
    public List<contentfwk_Control> getContentfwk_controls() {
        return contentfwk_controls;
    }

    public void addContentfwk_control(Contentfwk_control contentfwk_control) {
        this.contentfwk_controls.add(contentfwk_control);
    }
    public List<contentfwk_BusinessService> getContentfwk_businessservices() {
        return contentfwk_businessservices;
    }

    public void addContentfwk_businessservice(Contentfwk_businessservice contentfwk_businessservice) {
        this.contentfwk_businessservices.add(contentfwk_businessservice);
    }
    public List<contentfwk_Function> getContentfwk_functions() {
        return contentfwk_functions;
    }

    public void addContentfwk_function(Contentfwk_function contentfwk_function) {
        this.contentfwk_functions.add(contentfwk_function);
    }

}