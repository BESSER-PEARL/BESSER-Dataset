





import java.util.List;
import java.util.ArrayList;

public class simpleJava_class_declaration  {

    private String nomeClasse;





    private simpleJava_name simplejava_name;




    private List<simpleJava_name> simplejava_names;




    private List<simpleJava_class_declaration> simplejava_class_declarations;


    public simpleJava_class_declaration(
        String nomeClasse    ) {
        this.nomeClasse = nomeClasse;
        this.simplejava_names = new ArrayList<>();
        this.simplejava_class_declarations = new ArrayList<>();
    }

    public simpleJava_class_declaration(
        String nomeClasse        ArrayList<simpleJava_name> simplejava_names,        ArrayList<simpleJava_class_declaration> simplejava_class_declarations    ) {
        this.nomeClasse = nomeClasse;
        this.simplejava_names = simplejava_names;
        this.simplejava_class_declarations = simplejava_class_declarations;
    }

    public String getNomeclasse() {
        return nomeClasse;
    }

    public void setNomeclasse(String nomeClasse) {
        this.nomeClasse = nomeClasse;
    }

    public simpleJava_name getSimplejava_name() {
        return simplejava_name;
    }

    public void setSimplejava_name(simpleJava_name simplejava_name) {
        this.simplejava_name = simplejava_name;
    }
    public List<simpleJava_name> getSimplejava_names() {
        return simplejava_names;
    }

    public void addSimplejava_name(Simplejava_name simplejava_name) {
        this.simplejava_names.add(simplejava_name);
    }
    public List<simpleJava_class_declaration> getSimplejava_class_declarations() {
        return simplejava_class_declarations;
    }

    public void addSimplejava_class_declaration(Simplejava_class_declaration simplejava_class_declaration) {
        this.simplejava_class_declarations.add(simplejava_class_declaration);
    }

}