





import java.util.List;
import java.util.ArrayList;

public class gastm_CompilationUnit extends OtherSyntaxObject {

    private String language;





    private List<DefinitionObject> definitionobjects;


    public gastm_CompilationUnit(
        String language    ) {
        super(
        );
        this.language = language;
        this.definitionobjects = new ArrayList<>();
    }

    public gastm_CompilationUnit(
        String language        ArrayList<DefinitionObject> definitionobjects    ) {
        this.language = language;
        this.definitionobjects = definitionobjects;
    }

    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public List<DefinitionObject> getDefinitionobjects() {
        return definitionobjects;
    }

    public void addDefinitionobject(Definitionobject definitionobject) {
        this.definitionobjects.add(definitionobject);
    }

}