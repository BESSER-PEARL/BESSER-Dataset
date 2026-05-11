





import java.util.List;
import java.util.ArrayList;

public class service_Service extends NamedElement {






    private service_Selection service_selection;




    private List<service_Selection> service_selections;




    private List<service_BusinessOperation> service_businessoperations;




    private service_Selection service_selection;




    private service_BusinessOperation service_businessoperation;




    private service_BusinessOperation service_businessoperation;




    private service_Service service_service;




    private service_Selection service_selection;


    public service_Service(
    ) {
        super(
        );
        this.service_selections = new ArrayList<>();
        this.service_businessoperations = new ArrayList<>();
    }

    public service_Service(
        ArrayList<service_Selection> service_selections,        ArrayList<service_BusinessOperation> service_businessoperations    ) {
        this.service_selections = service_selections;
        this.service_businessoperations = service_businessoperations;
    }


    public service_Selection getService_selection() {
        return service_selection;
    }

    public void setService_selection(service_Selection service_selection) {
        this.service_selection = service_selection;
    }
    public List<service_Selection> getService_selections() {
        return service_selections;
    }

    public void addService_selection(Service_selection service_selection) {
        this.service_selections.add(service_selection);
    }
    public List<service_BusinessOperation> getService_businessoperations() {
        return service_businessoperations;
    }

    public void addService_businessoperation(Service_businessoperation service_businessoperation) {
        this.service_businessoperations.add(service_businessoperation);
    }
    public service_Selection getService_selection() {
        return service_selection;
    }

    public void setService_selection(service_Selection service_selection) {
        this.service_selection = service_selection;
    }
    public service_BusinessOperation getService_businessoperation() {
        return service_businessoperation;
    }

    public void setService_businessoperation(service_BusinessOperation service_businessoperation) {
        this.service_businessoperation = service_businessoperation;
    }
    public service_BusinessOperation getService_businessoperation() {
        return service_businessoperation;
    }

    public void setService_businessoperation(service_BusinessOperation service_businessoperation) {
        this.service_businessoperation = service_businessoperation;
    }
    public service_Service getService_service() {
        return service_service;
    }

    public void setService_service(service_Service service_service) {
        this.service_service = service_service;
    }
    public service_Selection getService_selection() {
        return service_selection;
    }

    public void setService_selection(service_Selection service_selection) {
        this.service_selection = service_selection;
    }

}