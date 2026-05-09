





import java.util.List;
import java.util.ArrayList;

public class Documentation_EmphasisValue extends ParagraphValue {

    private String value;
    private String role;



    public Documentation_EmphasisValue(
        String value,        String role    ) {
        super(
        );
        this.value = value;
        this.role = role;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }


}