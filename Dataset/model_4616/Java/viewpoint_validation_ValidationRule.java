





import java.util.List;
import java.util.ArrayList;

public class viewpoint_validation_ValidationRule  {

    private String level;
    private String message;



    public viewpoint_validation_ValidationRule(
        String level,        String message    ) {
        this.level = level;
        this.message = message;
    }


    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }


}