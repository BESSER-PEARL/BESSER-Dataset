





import java.util.List;
import java.util.ArrayList;

public class Documentation_EmphasisValue extends TextualValue, ParagraphValue {

    private String role;



    public Documentation_EmphasisValue(
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