





import java.util.List;
import java.util.ArrayList;

public class myDsl_BasicLit  {

    private String string_lit;
    private String float_lit;
    private String int_lit;
    private String imaginary_lit;
    private String rune_lit;





    private myDsl_Literal mydsl_literal;


    public myDsl_BasicLit(
        String string_lit,        String float_lit,        String int_lit,        String imaginary_lit,        String rune_lit    ) {
        this.string_lit = string_lit;
        this.float_lit = float_lit;
        this.int_lit = int_lit;
        this.imaginary_lit = imaginary_lit;
        this.rune_lit = rune_lit;
    }


    public String getString_lit() {
        return string_lit;
    }

    public void setString_lit(String string_lit) {
        this.string_lit = string_lit;
    }
    public String getFloat_lit() {
        return float_lit;
    }

    public void setFloat_lit(String float_lit) {
        this.float_lit = float_lit;
    }
    public String getInt_lit() {
        return int_lit;
    }

    public void setInt_lit(String int_lit) {
        this.int_lit = int_lit;
    }
    public String getImaginary_lit() {
        return imaginary_lit;
    }

    public void setImaginary_lit(String imaginary_lit) {
        this.imaginary_lit = imaginary_lit;
    }
    public String getRune_lit() {
        return rune_lit;
    }

    public void setRune_lit(String rune_lit) {
        this.rune_lit = rune_lit;
    }

    public myDsl_Literal getMydsl_literal() {
        return mydsl_literal;
    }

    public void setMydsl_literal(myDsl_Literal mydsl_literal) {
        this.mydsl_literal = mydsl_literal;
    }

}