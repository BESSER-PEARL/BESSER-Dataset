





import java.util.List;
import java.util.ArrayList;

public class timeBasedRouting_OccursModel  {

    private String description;
    private String mode;



    public timeBasedRouting_OccursModel(
        String description,        String mode    ) {
        this.description = description;
        this.mode = mode;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }


}