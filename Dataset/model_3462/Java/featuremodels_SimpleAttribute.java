





import java.util.List;
import java.util.ArrayList;

public class featuremodels_SimpleAttribute extends Attribute {

    private String value;
    private String type;



    public featuremodels_SimpleAttribute(
        String value,        String type    ) {
        super(
        );
        this.value = value;
        this.type = type;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}