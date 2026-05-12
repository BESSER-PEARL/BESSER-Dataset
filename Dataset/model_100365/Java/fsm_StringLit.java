





import java.util.List;
import java.util.ArrayList;

public class fsm_StringLit extends Literal {

    private String value;



    public fsm_StringLit(
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