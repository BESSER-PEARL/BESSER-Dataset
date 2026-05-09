





import java.util.List;
import java.util.ArrayList;

public class art_type_AbstractPort extends NamedElement {

    private String role;



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


}