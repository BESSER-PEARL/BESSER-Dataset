





import java.util.List;
import java.util.ArrayList;

public class dfa_State extends NamedElement {

    private String description;



    public dfa_State(
        String description    ) {
        super(
        );
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}