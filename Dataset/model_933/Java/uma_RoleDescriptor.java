





import java.util.List;
import java.util.ArrayList;

public class uma_RoleDescriptor extends Descriptor {

    private String responsibleFor;
    private String role;



    public uma_RoleDescriptor(
        String responsibleFor,        String role    ) {
        super(
        );
        this.responsibleFor = responsibleFor;
        this.role = role;
    }


    public String getResponsiblefor() {
        return responsibleFor;
    }

    public void setResponsiblefor(String responsibleFor) {
        this.responsibleFor = responsibleFor;
    }
    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }


}