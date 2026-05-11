





import java.util.List;
import java.util.ArrayList;

public class limp_FreshVariable extends Expr {

    private String value;



    public limp_FreshVariable(
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