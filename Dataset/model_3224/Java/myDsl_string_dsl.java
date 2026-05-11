





import java.util.List;
import java.util.ArrayList;

public class myDsl_string_dsl  {

    private String __func__;
    private String string_literal;



    public myDsl_string_dsl(
        String __func__,        String string_literal    ) {
        this.__func__ = __func__;
        this.string_literal = string_literal;
    }


    public String get__func__() {
        return __func__;
    }

    public void set__func__(String __func__) {
        this.__func__ = __func__;
    }
    public String getString_literal() {
        return string_literal;
    }

    public void setString_literal(String string_literal) {
        this.string_literal = string_literal;
    }


}