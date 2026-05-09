





import java.util.List;
import java.util.ArrayList;

public class gastm_EntryDefinition extends Definition {






    private List<FormalParameterDefinition> formalparameterdefinitions;




    private List<Statement> statements;


    public gastm_EntryDefinition(
    ) {
        super(
        );
        this.formalparameterdefinitions = new ArrayList<>();
        this.statements = new ArrayList<>();
    }

    public gastm_EntryDefinition(
        ArrayList<FormalParameterDefinition> formalparameterdefinitions,        ArrayList<Statement> statements    ) {
        this.formalparameterdefinitions = formalparameterdefinitions;
        this.statements = statements;
    }


    public List<FormalParameterDefinition> getFormalparameterdefinitions() {
        return formalparameterdefinitions;
    }

    public void addFormalparameterdefinition(Formalparameterdefinition formalparameterdefinition) {
        this.formalparameterdefinitions.add(formalparameterdefinition);
    }
    public List<Statement> getStatements() {
        return statements;
    }

    public void addStatement(Statement statement) {
        this.statements.add(statement);
    }

}