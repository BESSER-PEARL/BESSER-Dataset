





import java.util.List;
import java.util.ArrayList;

public class sADL_PrintStatement extends SadlModelElement {

    private String model;
    private String displayString;



    public sADL_PrintStatement(
        String model,        String displayString    ) {
        super(
        );
        this.model = model;
        this.displayString = displayString;
    }


    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }
    public String getDisplaystring() {
        return displayString;
    }

    public void setDisplaystring(String displayString) {
        this.displayString = displayString;
    }


}