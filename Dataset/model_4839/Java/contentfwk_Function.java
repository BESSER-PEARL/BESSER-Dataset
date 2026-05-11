





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Function extends Standard, Element {






    private List<contentfwk_Service> contentfwk_services;




    private contentfwk_Function contentfwk_function;




    private contentfwk_Service contentfwk_service;




    private List<contentfwk_Function> contentfwk_functions;


    public contentfwk_Function(
    ) {
        super(
        );
        this.contentfwk_services = new ArrayList<>();
        this.contentfwk_functions = new ArrayList<>();
    }

    public contentfwk_Function(
        ArrayList<contentfwk_Service> contentfwk_services,        ArrayList<contentfwk_Function> contentfwk_functions    ) {
        this.contentfwk_services = contentfwk_services;
        this.contentfwk_functions = contentfwk_functions;
    }


    public List<contentfwk_Service> getContentfwk_services() {
        return contentfwk_services;
    }

    public void addContentfwk_service(Contentfwk_service contentfwk_service) {
        this.contentfwk_services.add(contentfwk_service);
    }
    public contentfwk_Function getContentfwk_function() {
        return contentfwk_function;
    }

    public void setContentfwk_function(contentfwk_Function contentfwk_function) {
        this.contentfwk_function = contentfwk_function;
    }
    public contentfwk_Service getContentfwk_service() {
        return contentfwk_service;
    }

    public void setContentfwk_service(contentfwk_Service contentfwk_service) {
        this.contentfwk_service = contentfwk_service;
    }
    public List<contentfwk_Function> getContentfwk_functions() {
        return contentfwk_functions;
    }

    public void addContentfwk_function(Contentfwk_function contentfwk_function) {
        this.contentfwk_functions.add(contentfwk_function);
    }

}