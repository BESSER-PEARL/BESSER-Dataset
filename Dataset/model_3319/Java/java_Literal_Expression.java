





import java.util.List;
import java.util.ArrayList;

public class java_Literal_Expression extends Return_value {

    private String char;
    private String exp;
    private int exp1;
    private String string;



    public java_Literal_Expression(
        String char,        String exp,        int exp1,        String string    ) {
        super(
        );
        this.char = char;
        this.exp = exp;
        this.exp1 = exp1;
        this.string = string;
    }


    public String getChar() {
        return char;
    }

    public void setChar(String char) {
        this.char = char;
    }
    public String getExp() {
        return exp;
    }

    public void setExp(String exp) {
        this.exp = exp;
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