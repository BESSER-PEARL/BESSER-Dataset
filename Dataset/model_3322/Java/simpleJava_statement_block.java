





import java.util.List;
import java.util.ArrayList;

public class simpleJava_statement_block  {






    private simpleJava_variable_declaration simplejava_variable_declaration;




    private simpleJava_method_declaration simplejava_method_declaration;




    private simpleJava_statement simplejava_statement;




    private simpleJava_constructor_declaration simplejava_constructor_declaration;




    private List<simpleJava_statement> simplejava_statements;




    private simpleJava_static_initializer simplejava_static_initializer;


    public simpleJava_statement_block(
    ) {
        this.simplejava_statements = new ArrayList<>();
    }

    public simpleJava_statement_block(
        ArrayList<simpleJava_statement> simplejava_statements    ) {
        this.simplejava_statements = simplejava_statements;
    }


    public simpleJava_variable_declaration getSimplejava_variable_declaration() {
        return simplejava_variable_declaration;
    }

    public void setSimplejava_variable_declaration(simpleJava_variable_declaration simplejava_variable_declaration) {
        this.simplejava_variable_declaration = simplejava_variable_declaration;
    }
    public simpleJava_method_declaration getSimplejava_method_declaration() {
        return simplejava_method_declaration;
    }

    public void setSimplejava_method_declaration(simpleJava_method_declaration simplejava_method_declaration) {
        this.simplejava_method_declaration = simplejava_method_declaration;
    }
    public simpleJava_statement getSimplejava_statement() {
        return simplejava_statement;
    }

    public void setSimplejava_statement(simpleJava_statement simplejava_statement) {
        this.simplejava_statement = simplejava_statement;
    }
    public simpleJava_constructor_declaration getSimplejava_constructor_declaration() {
        return simplejava_constructor_declaration;
    }

    public void setSimplejava_constructor_declaration(simpleJava_constructor_declaration simplejava_constructor_declaration) {
        this.simplejava_constructor_declaration = simplejava_constructor_declaration;
    }
    public List<simpleJava_statement> getSimplejava_statements() {
        return simplejava_statements;
    }

    public void addSimplejava_statement(Simplejava_statement simplejava_statement) {
        this.simplejava_statements.add(simplejava_statement);
    }
    public simpleJava_static_initializer getSimplejava_static_initializer() {
        return simplejava_static_initializer;
    }

    public void setSimplejava_static_initializer(simpleJava_static_initializer simplejava_static_initializer) {
        this.simplejava_static_initializer = simplejava_static_initializer;
    }

}