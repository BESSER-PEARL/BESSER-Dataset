





import java.util.List;
import java.util.ArrayList;

public class dbl_StringLiteral extends L1Expr {

    private String value;



    public dbl_StringLiteral(
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