





import java.util.List;
import java.util.ArrayList;

public class simple200_Variable extends Thing {

    private String type;
    private String value;





    private simple200_State simple200_state;


    public simple200_Variable(
        String type,        String value    ) {
        super(
        );
        this.type = type;
        this.value = value;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public simple200_State getSimple200_state() {
        return simple200_state;
    }

    public void setSimple200_state(simple200_State simple200_state) {
        this.simple200_state = simple200_state;
    }

}