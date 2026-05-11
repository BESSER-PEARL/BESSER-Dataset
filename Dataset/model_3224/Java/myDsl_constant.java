





import java.util.List;
import java.util.ArrayList;

public class myDsl_constant  {

    private int i_constant;
    private String string;
    private String f_constant;
    private String enumz;
    private String char;





    private myDsl_primary_expression mydsl_primary_expression;


    public myDsl_constant(
        int i_constant,        String string,        String f_constant,        String enumz,        String char    ) {
        this.i_constant = i_constant;
        this.string = string;
        this.f_constant = f_constant;
        this.enumz = enumz;
        this.char = char;
    }


    public int getI_constant() {
        return i_constant;
    }

    public void setI_constant(int i_constant) {
        this.i_constant = i_constant;
    }
    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }
    public String getF_constant() {
        return f_constant;
    }

    public void setF_constant(String f_constant) {
        this.f_constant = f_constant;
    }
    public String getEnumz() {
        return enumz;
    }

    public void setEnumz(String enumz) {
        this.enumz = enumz;
    }
    public String getChar() {
        return char;
    }

    public void setChar(String char) {
        this.char = char;
    }

    public myDsl_primary_expression getMydsl_primary_expression() {
        return mydsl_primary_expression;
    }

    public void setMydsl_primary_expression(myDsl_primary_expression mydsl_primary_expression) {
        this.mydsl_primary_expression = mydsl_primary_expression;
    }

}