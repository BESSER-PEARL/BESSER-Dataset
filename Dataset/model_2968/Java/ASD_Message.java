





import java.util.List;
import java.util.ArrayList;

public class ASD_Message extends NamedElement {

    private String subset;
    private String role;



    public ASD_Message(
        String subset,        String role    ) {
        super(
        );
        this.subset = subset;
        this.role = role;
    }


    public String getSubset() {
        return subset;
    }

    public void setSubset(String subset) {
        this.subset = subset;
    }
    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }


}