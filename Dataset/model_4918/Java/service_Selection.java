





import java.util.List;
import java.util.ArrayList;

public class service_Selection extends FormalParameterList, NamedElement {

    private int limit;
    private boolean distinct;
    private boolean selected;





    private service_Service service_service;




    private service_Service service_service;


    public service_Selection(
        int limit,        boolean distinct,        boolean selected    ) {
        super(
        );
        this.limit = limit;
        this.distinct = distinct;
        this.selected = selected;
    }


    public int getLimit() {
        return limit;
    }

    public void setLimit(int limit) {
        this.limit = limit;
    }
    public boolean getDistinct() {
        return distinct;
    }

    public void setDistinct(boolean distinct) {
        this.distinct = distinct;
    }
    public boolean getSelected() {
        return selected;
    }

    public void setSelected(boolean selected) {
        this.selected = selected;
    }

    public service_Service getService_service() {
        return service_service;
    }

    public void setService_service(service_Service service_service) {
        this.service_service = service_service;
    }
    public service_Service getService_service() {
        return service_service;
    }

    public void setService_service(service_Service service_service) {
        this.service_service = service_service;
    }

}