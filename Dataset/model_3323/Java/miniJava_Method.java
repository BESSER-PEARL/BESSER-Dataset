





import java.util.List;
import java.util.ArrayList;

public class miniJava_Method  {

    private String name;





    private List<miniJava_VarDeclaration> minijava_vardeclarations;




    private miniJava_ClassDecl minijava_classdecl;


    public miniJava_Method(
        String name    ) {
        this.name = name;
        this.minijava_vardeclarations = new ArrayList<>();
    }

    public miniJava_Method(
        String name        ArrayList<miniJava_VarDeclaration> minijava_vardeclarations    ) {
        this.name = name;
        this.minijava_vardeclarations = minijava_vardeclarations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<miniJava_VarDeclaration> getMinijava_vardeclarations() {
        return minijava_vardeclarations;
    }

    public void addMinijava_vardeclaration(Minijava_vardeclaration minijava_vardeclaration) {
        this.minijava_vardeclarations.add(minijava_vardeclaration);
    }
    public miniJava_ClassDecl getMinijava_classdecl() {
        return minijava_classdecl;
    }

    public void setMinijava_classdecl(miniJava_ClassDecl minijava_classdecl) {
        this.minijava_classdecl = minijava_classdecl;
    }

}