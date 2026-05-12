





import java.util.List;
import java.util.ArrayList;

public class fmpl_StringLit extends Literal {

    private String value;



    public fmpl_StringLit(
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