





import java.util.List;
import java.util.ArrayList;

public class java_StringReference extends Reference {

    private String value;



    public java_StringReference(
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