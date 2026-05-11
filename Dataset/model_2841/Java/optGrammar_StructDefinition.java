





import java.util.List;
import java.util.ArrayList;

public class optGrammar_StructDefinition extends DefinitionBody {

    private String name;





    private List<optGrammar_PrimaryTypeDefinitionDeclaration> optgrammar_primarytypedefinitiondeclarations;


    public optGrammar_StructDefinition(
        String name    ) {
        super(
        );
        this.name = name;
        this.optgrammar_primarytypedefinitiondeclarations = new ArrayList<>();
    }

    public optGrammar_StructDefinition(
        String name        ArrayList<optGrammar_PrimaryTypeDefinitionDeclaration> optgrammar_primarytypedefinitiondeclarations    ) {
        this.name = name;
        this.optgrammar_primarytypedefinitiondeclarations = optgrammar_primarytypedefinitiondeclarations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<optGrammar_PrimaryTypeDefinitionDeclaration> getOptgrammar_primarytypedefinitiondeclarations() {
        return optgrammar_primarytypedefinitiondeclarations;
    }

    public void addOptgrammar_primarytypedefinitiondeclaration(Optgrammar_primarytypedefinitiondeclaration optgrammar_primarytypedefinitiondeclaration) {
        this.optgrammar_primarytypedefinitiondeclarations.add(optgrammar_primarytypedefinitiondeclaration);
    }

}