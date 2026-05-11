





import java.util.List;
import java.util.ArrayList;

public class myDsl_string_nova  {

    private String string_literal;
    private String func_name;



    public myDsl_string_nova(
        String string_literal,        String func_name    ) {
        this.string_literal = string_literal;
        this.func_name = func_name;
    }


    public String getString_literal() {
        return string_literal;
    }

    public void setString_literal(String string_literal) {
        this.string_literal = string_literal;
    }
    public String getFunc_name() {
        return func_name;
    }

    public void setFunc_name(String func_name) {
        this.func_name = func_name;
    }


}