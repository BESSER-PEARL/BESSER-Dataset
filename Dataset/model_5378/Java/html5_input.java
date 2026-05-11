





import java.util.List;
import java.util.ArrayList;

public class html5_input extends htmlElement {

    private String value;
    private String disable;
    private String type;



    public html5_input(
        String value,        String disable,        String type    ) {
        super(
        );
        this.value = value;
        this.disable = disable;
        this.type = type;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getDisable() {
        return disable;
    }

    public void setDisable(String disable) {
        this.disable = disable;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}