





import java.util.List;
import java.util.ArrayList;

public class myDsl_multiplicative_expression_complement  {

    private String modulo;
    private String divide;
    private String multiplica;





    private myDsl_multiplicative_expression_linha mydsl_multiplicative_expression_linha;




    private myDsl_cast_expression mydsl_cast_expression;


    public myDsl_multiplicative_expression_complement(
        String modulo,        String divide,        String multiplica    ) {
        this.modulo = modulo;
        this.divide = divide;
        this.multiplica = multiplica;
    }


    public String getModulo() {
        return modulo;
    }

    public void setModulo(String modulo) {
        this.modulo = modulo;
    }
    public String getDivide() {
        return divide;
    }

    public void setDivide(String divide) {
        this.divide = divide;
    }
    public String getMultiplica() {
        return multiplica;
    }

    public void setMultiplica(String multiplica) {
        this.multiplica = multiplica;
    }

    public myDsl_multiplicative_expression_linha getMydsl_multiplicative_expression_linha() {
        return mydsl_multiplicative_expression_linha;
    }

    public void setMydsl_multiplicative_expression_linha(myDsl_multiplicative_expression_linha mydsl_multiplicative_expression_linha) {
        this.mydsl_multiplicative_expression_linha = mydsl_multiplicative_expression_linha;
    }
    public myDsl_cast_expression getMydsl_cast_expression() {
        return mydsl_cast_expression;
    }

    public void setMydsl_cast_expression(myDsl_cast_expression mydsl_cast_expression) {
        this.mydsl_cast_expression = mydsl_cast_expression;
    }

}