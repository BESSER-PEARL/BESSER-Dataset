





import java.util.List;
import java.util.ArrayList;

public class graph_StringConstant extends Expr {

    private String value;



    public graph_StringConstant(
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