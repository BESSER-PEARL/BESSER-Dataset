





import java.util.List;
import java.util.ArrayList;

public class simpleJava_literal_expression  {

    private String inteiro;
    private String decimal;
    private String l_float;
    private String string;





    private simpleJava_expression simplejava_expression;


    public simpleJava_literal_expression(
        String inteiro,        String decimal,        String l_float,        String string    ) {
        this.inteiro = inteiro;
        this.decimal = decimal;
        this.l_float = l_float;
        this.string = string;
    }


    public String getInteiro() {
        return inteiro;
    }

    public void setInteiro(String inteiro) {
        this.inteiro = inteiro;
    }
    public String getDecimal() {
        return decimal;
    }

    public void setDecimal(String decimal) {
        this.decimal = decimal;
    }
    public String getL_float() {
        return l_float;
    }

    public void setL_float(String l_float) {
        this.l_float = l_float;
    }
    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }

    public simpleJava_expression getSimplejava_expression() {
        return simplejava_expression;
    }

    public void setSimplejava_expression(simpleJava_expression simplejava_expression) {
        this.simplejava_expression = simplejava_expression;
    }

}