





import java.util.List;
import java.util.ArrayList;

public class java_Literal_Expression extends Return_value {

    private String exp;
    private String char;
    private int exp1;
    private String string;



    public java_Literal_Expression(
        String exp,        String char,        int exp1,        String string    ) {
        super(
        );
        this.exp = exp;
        this.char = char;
        this.exp1 = exp1;
        this.string = string;
    }


    public String getExp() {
        return exp;
    }

    public void setExp(String exp) {
        this.exp = exp;
    }
    public String getChar() {
        return char;
    }

    public void setChar(String char) {
        this.char = char;
    }
    public int getExp1() {
        return exp1;
    }

    public void setExp1(int exp1) {
        this.exp1 = exp1;
    }
    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }


}