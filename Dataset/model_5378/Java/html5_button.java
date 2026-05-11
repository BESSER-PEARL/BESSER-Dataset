





import java.util.List;
import java.util.ArrayList;

public class html5_button extends htmlElement {

    private String value;
    private String action;
    private String type;



    public html5_button(
        String value,        String action,        String type    ) {
        super(
        );
        this.value = value;
        this.action = action;
        this.type = type;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}