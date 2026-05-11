





import java.util.List;
import java.util.ArrayList;

public class jcl_statements_Command extends Statement {

    private String value;



    public jcl_statements_Command(
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