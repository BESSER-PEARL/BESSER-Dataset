





import java.util.List;
import java.util.ArrayList;

public class simpleJava_mais_aux  {

    private String operador;





    private simpleJava_expression_aux simplejava_expression_aux;


    public simpleJava_mais_aux(
        String operador    ) {
        this.operador = operador;
    }


    public String getOperador() {
        return operador;
    }

    public void setOperador(String operador) {
        this.operador = operador;
    }

    public simpleJava_expression_aux getSimplejava_expression_aux() {
        return simplejava_expression_aux;
    }

    public void setSimplejava_expression_aux(simpleJava_expression_aux simplejava_expression_aux) {
        this.simplejava_expression_aux = simplejava_expression_aux;
    }

}