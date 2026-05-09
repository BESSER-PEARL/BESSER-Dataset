





import java.util.List;
import java.util.ArrayList;

public class uma_RoleDescriptor extends Descriptor {

    private String role;
    private String responsibleFor;



    public uma_RoleDescriptor(
        String role,        String responsibleFor    ) {
        super(
        );
        this.role = role;
        this.responsibleFor = responsibleFor;
    }


    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }
    public String getResponsiblefor() {
        return responsibleFor;
    }

    public void setResponsiblefor(String responsibleFor) {
        this.responsibleFor = responsibleFor;
    }


}