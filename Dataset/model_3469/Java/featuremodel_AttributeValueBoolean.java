





import java.util.List;
import java.util.ArrayList;

public class featuremodel_AttributeValueBoolean extends AttributeValue {

    private boolean value;



    public featuremodel_AttributeValueBoolean(
        boolean value    ) {
        super(
        );
        this.value = value;
    }


    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }


}