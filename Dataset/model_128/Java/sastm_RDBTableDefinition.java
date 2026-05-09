





import java.util.List;
import java.util.ArrayList;

public class sastm_RDBTableDefinition extends Definition {






    private List<DeclarationOrDefinition> declarationordefinitions;




    private List<CompilationUnit> compilationunits;




    private List<GASTMObject> gastmobjects;


    public sastm_RDBTableDefinition(
    ) {
        super(
        );
        this.declarationordefinitions = new ArrayList<>();
        this.compilationunits = new ArrayList<>();
        this.gastmobjects = new ArrayList<>();
    }

    public sastm_RDBTableDefinition(
        ArrayList<DeclarationOrDefinition> declarationordefinitions,        ArrayList<CompilationUnit> compilationunits,        ArrayList<GASTMObject> gastmobjects    ) {
        this.declarationordefinitions = declarationordefinitions;
        this.compilationunits = compilationunits;
        this.gastmobjects = gastmobjects;
    }


    public List<DeclarationOrDefinition> getDeclarationordefinitions() {
        return declarationordefinitions;
    }

    public void addDeclarationordefinition(Declarationordefinition declarationordefinition) {
        this.declarationordefinitions.add(declarationordefinition);
    }
    public List<CompilationUnit> getCompilationunits() {
        return compilationunits;
    }

    public void addCompilationunit(Compilationunit compilationunit) {
        this.compilationunits.add(compilationunit);
    }
    public List<GASTMObject> getGastmobjects() {
        return gastmobjects;
    }

    public void addGastmobject(Gastmobject gastmobject) {
        this.gastmobjects.add(gastmobject);
    }

}