





import java.util.List;
import java.util.ArrayList;

public class MocaTree_Attribute extends TreeElement {

    private String value;



    public MocaTree_Attribute(
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