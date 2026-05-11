





import java.util.List;
import java.util.ArrayList;

public class simpleJava_method_declaration  {

    private String nomeMetodo;





    private simpleJava_MODIFIER simplejava_modifier;




    private simpleJava_field_declaration simplejava_field_declaration;


    public simpleJava_method_declaration(
        String nomeMetodo    ) {
        this.nomeMetodo = nomeMetodo;
    }


    public String getNomemetodo() {
        return nomeMetodo;
    }

    public void setNomemetodo(String nomeMetodo) {
        this.nomeMetodo = nomeMetodo;
    }

    public simpleJava_MODIFIER getSimplejava_modifier() {
        return simplejava_modifier;
    }

    public void setSimplejava_modifier(simpleJava_MODIFIER simplejava_modifier) {
        this.simplejava_modifier = simplejava_modifier;
    }
    public simpleJava_field_declaration getSimplejava_field_declaration() {
        return simplejava_field_declaration;
    }

    public void setSimplejava_field_declaration(simpleJava_field_declaration simplejava_field_declaration) {
        this.simplejava_field_declaration = simplejava_field_declaration;
    }

}