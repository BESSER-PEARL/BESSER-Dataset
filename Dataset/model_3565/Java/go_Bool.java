





import java.util.List;
import java.util.ArrayList;

public class go_Bool extends TypeValue {

    private String val;





    private go_Literal go_literal;


    public go_Bool(
        String val    ) {
        super(
        );
        this.val = val;
    }


    public String getVal() {
        return val;
    }

    public void setVal(String val) {
        this.val = val;
    }

    public go_Literal getGo_literal() {
        return go_literal;
    }

    public void setGo_literal(go_Literal go_literal) {
        this.go_literal = go_literal;
    }

}