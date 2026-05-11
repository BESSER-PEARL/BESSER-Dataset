





import java.util.List;
import java.util.ArrayList;

public class myDsl_Literal_Expression  {

    private String charLit;
    private String string;
    private String exp;
    private int exp1;





    private myDsl_Expression mydsl_expression;


    public myDsl_Literal_Expression(
        String charLit,        String string,        String exp,        int exp1    ) {
        this.charLit = charLit;
        this.string = string;
        this.exp = exp;
        this.exp1 = exp1;
    }


    public String getCharlit() {
        return charLit;
    }

    public void setCharlit(String charLit) {
        this.charLit = charLit;
    }
    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
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

    public myDsl_Expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_Expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }

}