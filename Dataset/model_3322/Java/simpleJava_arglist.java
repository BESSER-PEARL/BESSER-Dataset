





import java.util.List;
import java.util.ArrayList;

public class simpleJava_arglist extends variable_declarator {

    private String nomeParametro;





    private List<simpleJava_type> simplejava_types;




    private simpleJava_expression_aux simplejava_expression_aux;




    private List<simpleJava_expression> simplejava_expressions;


    public simpleJava_arglist(
        String nomeParametro    ) {
        super(
        );
        this.nomeParametro = nomeParametro;
        this.simplejava_types = new ArrayList<>();
        this.simplejava_expressions = new ArrayList<>();
    }

    public simpleJava_arglist(
        String nomeParametro        ArrayList<simpleJava_type> simplejava_types,        ArrayList<simpleJava_expression> simplejava_expressions    ) {
        this.nomeParametro = nomeParametro;
        this.simplejava_types = simplejava_types;
        this.simplejava_expressions = simplejava_expressions;
    }

    public String getNomeparametro() {
        return nomeParametro;
    }

    public void setNomeparametro(String nomeParametro) {
        this.nomeParametro = nomeParametro;
    }

    public List<simpleJava_type> getSimplejava_types() {
        return simplejava_types;
    }

    public void addSimplejava_type(Simplejava_type simplejava_type) {
        this.simplejava_types.add(simplejava_type);
    }
    public simpleJava_expression_aux getSimplejava_expression_aux() {
        return simplejava_expression_aux;
    }

    public void setSimplejava_expression_aux(simpleJava_expression_aux simplejava_expression_aux) {
        this.simplejava_expression_aux = simplejava_expression_aux;
    }
    public List<simpleJava_expression> getSimplejava_expressions() {
        return simplejava_expressions;
    }

    public void addSimplejava_expression(Simplejava_expression simplejava_expression) {
        this.simplejava_expressions.add(simplejava_expression);
    }

}