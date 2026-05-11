





import java.util.List;
import java.util.ArrayList;

public class myDsl_static_assert_declaration  {

    private String string_literal;
    private String static_assert;



    public myDsl_static_assert_declaration(
        String string_literal,        String static_assert    ) {
        this.string_literal = string_literal;
        this.static_assert = static_assert;
    }


    public String getString_literal() {
        return string_literal;
    }

    public void setString_literal(String string_literal) {
        this.string_literal = string_literal;
    }
    public String getStatic_assert() {
        return static_assert;
    }

    public void setStatic_assert(String static_assert) {
        this.static_assert = static_assert;
    }


}