





import java.util.List;
import java.util.ArrayList;

public class sadl_Display extends ModelElement {

    private String displayString;
    private String model;



    public sadl_Display(
        String displayString,        String model    ) {
        super(
        );
        this.displayString = displayString;
        this.model = model;
    }


    public String getDisplaystring() {
        return displayString;
    }

    public void setDisplaystring(String displayString) {
        this.displayString = displayString;
    }
    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }


}