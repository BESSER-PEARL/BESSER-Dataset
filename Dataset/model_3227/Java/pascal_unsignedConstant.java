





import java.util.List;
import java.util.ArrayList;

public class pascal_unsignedConstant  {

    private String string_literal;





    private pascal_factor pascal_factor;


    public pascal_unsignedConstant(
        String string_literal    ) {
        this.string_literal = string_literal;
    }


    public String getString_literal() {
        return string_literal;
    }

    public void setString_literal(String string_literal) {
        this.string_literal = string_literal;
    }

    public pascal_factor getPascal_factor() {
        return pascal_factor;
    }

    public void setPascal_factor(pascal_factor pascal_factor) {
        this.pascal_factor = pascal_factor;
    }

}