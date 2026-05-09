





import java.util.List;
import java.util.ArrayList;

public class eTJ_Macro extends Property {

    private String value;
    private String id;



    public eTJ_Macro(
        String value,        String id    ) {
        super(
        );
        this.value = value;
        this.id = id;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}