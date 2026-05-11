





import java.util.List;
import java.util.ArrayList;

public class dsl_Abort extends Action {

    private String value;



    public dsl_Abort(
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