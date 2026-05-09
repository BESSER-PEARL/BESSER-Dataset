





import java.util.List;
import java.util.ArrayList;

public class art_type_AbstractPort extends NamedElement {

    private String role;





    private Service service;


    public art_type_AbstractPort(
        String role    ) {
        super(
        );
        this.role = role;
    }


    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }

    public Service getService() {
        return service;
    }

    public void setService(Service service) {
        this.service = service;
    }

}