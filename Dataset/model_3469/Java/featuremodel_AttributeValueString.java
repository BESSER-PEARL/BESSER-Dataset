





import java.util.List;
import java.util.ArrayList;

public class featuremodel_AttributeValueString extends AttributeValue {

    private String value;



    public featuremodel_AttributeValueString(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}