





import java.util.List;
import java.util.ArrayList;

public class viewpoint_validation_ValidationRule extends IdentifiedElement {

    private String message;
    private String level;



    public viewpoint_validation_ValidationRule(
        String message,        String level    ) {
        super(
        );
        this.message = message;
        this.level = level;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }


}