





import java.util.List;
import java.util.ArrayList;

public class featuremodel_AttributeValueInt extends AttributeValue {

    private int value;



    public featuremodel_AttributeValueInt(
        int value    ) {
        super(
        );
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}