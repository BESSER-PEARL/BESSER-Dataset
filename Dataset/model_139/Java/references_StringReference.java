





import java.util.List;
import java.util.ArrayList;

public class references_StringReference extends Reference {

    private String value;



    public references_StringReference(
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