





import java.util.List;
import java.util.ArrayList;

public class javali_Record  {






    private javali_Identifier javali_identifier;




    private List<javali_VarDeclaration> javali_vardeclarations;




    private javali_Module javali_module;


    public javali_Record(
    ) {
        this.javali_vardeclarations = new ArrayList<>();
    }

    public javali_Record(
        ArrayList<javali_VarDeclaration> javali_vardeclarations    ) {
        this.javali_vardeclarations = javali_vardeclarations;
    }


    public javali_Identifier getJavali_identifier() {
        return javali_identifier;
    }

    public void setJavali_identifier(javali_Identifier javali_identifier) {
        this.javali_identifier = javali_identifier;
    }
    public List<javali_VarDeclaration> getJavali_vardeclarations() {
        return javali_vardeclarations;
    }

    public void addJavali_vardeclaration(Javali_vardeclaration javali_vardeclaration) {
        this.javali_vardeclarations.add(javali_vardeclaration);
    }
    public javali_Module getJavali_module() {
        return javali_module;
    }

    public void setJavali_module(javali_Module javali_module) {
        this.javali_module = javali_module;
    }

}