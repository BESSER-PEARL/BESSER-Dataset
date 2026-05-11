





import java.util.List;
import java.util.ArrayList;

public class go_BasicLit  {

    private String int_lit;





    private go_Literal go_literal;




    private go_string_lit go_string_lit;


    public go_BasicLit(
        String int_lit    ) {
        this.int_lit = int_lit;
    }


    public String getInt_lit() {
        return int_lit;
    }

    public void setInt_lit(String int_lit) {
        this.int_lit = int_lit;
    }

    public go_Literal getGo_literal() {
        return go_literal;
    }

    public void setGo_literal(go_Literal go_literal) {
        this.go_literal = go_literal;
    }
    public go_string_lit getGo_string_lit() {
        return go_string_lit;
    }

    public void setGo_string_lit(go_string_lit go_string_lit) {
        this.go_string_lit = go_string_lit;
    }

}