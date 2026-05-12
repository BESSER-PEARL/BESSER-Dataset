





import java.util.List;
import java.util.ArrayList;

public class operators_ASSIGN extends Operator {

    private String value;



    public operators_ASSIGN(
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