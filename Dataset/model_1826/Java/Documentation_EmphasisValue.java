





import java.util.List;
import java.util.ArrayList;

public class Documentation_EmphasisValue extends ParagraphValue {

    private String role;
    private String value;



    public Documentation_EmphasisValue(
        String role,        String value    ) {
        super(
        );
        this.role = role;
        this.value = value;
    }


    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}