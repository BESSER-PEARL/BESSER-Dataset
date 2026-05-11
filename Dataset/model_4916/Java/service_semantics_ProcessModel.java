





import java.util.List;
import java.util.ArrayList;

public class service_semantics_ProcessModel extends IOEP {

    private String name;





    private semantics_service_Service semantics_service_service;


    public service_semantics_ProcessModel(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public semantics_service_Service getSemantics_service_service() {
        return semantics_service_service;
    }

    public void setSemantics_service_service(semantics_service_Service semantics_service_service) {
        this.semantics_service_service = semantics_service_service;
    }

}