





import java.util.List;
import java.util.ArrayList;

public class simpleJava_variable_declarator  {

    private String nomeVariavel;
    private String op;





    private simpleJava_variable_declaration simplejava_variable_declaration;


    public simpleJava_variable_declarator(
        String nomeVariavel,        String op    ) {
        this.nomeVariavel = nomeVariavel;
        this.op = op;
    }


    public String getNomevariavel() {
        return nomeVariavel;
    }

    public void setNomevariavel(String nomeVariavel) {
        this.nomeVariavel = nomeVariavel;
    }
    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public simpleJava_variable_declaration getSimplejava_variable_declaration() {
        return simplejava_variable_declaration;
    }

    public void setSimplejava_variable_declaration(simpleJava_variable_declaration simplejava_variable_declaration) {
        this.simplejava_variable_declaration = simplejava_variable_declaration;
    }

}