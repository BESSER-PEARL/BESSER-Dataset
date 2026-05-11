





import java.util.List;
import java.util.ArrayList;

public class simpleJava_variable_initializer  {






    private simpleJava_variable_declarator simplejava_variable_declarator;




    private List<simpleJava_variable_initializer> simplejava_variable_initializers;




    private simpleJava_expression simplejava_expression;


    public simpleJava_variable_initializer(
    ) {
        this.simplejava_variable_initializers = new ArrayList<>();
    }

    public simpleJava_variable_initializer(
        ArrayList<simpleJava_variable_initializer> simplejava_variable_initializers    ) {
        this.simplejava_variable_initializers = simplejava_variable_initializers;
    }


    public simpleJava_variable_declarator getSimplejava_variable_declarator() {
        return simplejava_variable_declarator;
    }

    public void setSimplejava_variable_declarator(simpleJava_variable_declarator simplejava_variable_declarator) {
        this.simplejava_variable_declarator = simplejava_variable_declarator;
    }
    public List<simpleJava_variable_initializer> getSimplejava_variable_initializers() {
        return simplejava_variable_initializers;
    }

    public void addSimplejava_variable_initializer(Simplejava_variable_initializer simplejava_variable_initializer) {
        this.simplejava_variable_initializers.add(simplejava_variable_initializer);
    }
    public simpleJava_expression getSimplejava_expression() {
        return simplejava_expression;
    }

    public void setSimplejava_expression(simpleJava_expression simplejava_expression) {
        this.simplejava_expression = simplejava_expression;
    }

}