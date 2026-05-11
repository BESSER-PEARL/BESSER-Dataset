





import java.util.List;
import java.util.ArrayList;

public class webapp_CheckBox extends FormWidget {

    private String description;



    public webapp_CheckBox(
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