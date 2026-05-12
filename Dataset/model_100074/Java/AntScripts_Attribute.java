





import java.util.List;
import java.util.ArrayList;

public class AntScripts_Attribute extends NamedElement {

    private String value;



    public AntScripts_Attribute(
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