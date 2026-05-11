





import java.util.List;
import java.util.ArrayList;

public class miniJava_Program  {

    private String name;





    private List<miniJava_TypeDeclaration> minijava_typedeclarations;




    private miniJava_State minijava_state;




    private List<miniJava_Import> minijava_imports;


    public miniJava_Program(
        String name    ) {
        this.name = name;
        this.minijava_typedeclarations = new ArrayList<>();
        this.minijava_imports = new ArrayList<>();
    }

    public miniJava_Program(
        String name        ArrayList<miniJava_TypeDeclaration> minijava_typedeclarations,        ArrayList<miniJava_Import> minijava_imports    ) {
        this.name = name;
        this.minijava_typedeclarations = minijava_typedeclarations;
        this.minijava_imports = minijava_imports;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<miniJava_TypeDeclaration> getMinijava_typedeclarations() {
        return minijava_typedeclarations;
    }

    public void addMinijava_typedeclaration(Minijava_typedeclaration minijava_typedeclaration) {
        this.minijava_typedeclarations.add(minijava_typedeclaration);
    }
    public miniJava_State getMinijava_state() {
        return minijava_state;
    }

    public void setMinijava_state(miniJava_State minijava_state) {
        this.minijava_state = minijava_state;
    }
    public List<miniJava_Import> getMinijava_imports() {
        return minijava_imports;
    }

    public void addMinijava_import(Minijava_import minijava_import) {
        this.minijava_imports.add(minijava_import);
    }

}