





import java.util.List;
import java.util.ArrayList;

public class imp_StringConst extends Expr {

    private String value;



    public imp_StringConst(
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