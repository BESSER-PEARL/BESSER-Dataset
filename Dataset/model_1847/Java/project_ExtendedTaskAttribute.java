





import java.util.List;
import java.util.ArrayList;

public class project_ExtendedTaskAttribute extends TaskAttribute {

    private String value;



    public project_ExtendedTaskAttribute(
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