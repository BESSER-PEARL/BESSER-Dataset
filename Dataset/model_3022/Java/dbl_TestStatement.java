





import java.util.List;
import java.util.ArrayList;

public class dbl_TestStatement extends Statement {

    private String value;



    public dbl_TestStatement(
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