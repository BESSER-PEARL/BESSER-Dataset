





import java.util.List;
import java.util.ArrayList;

public class astm_gastm_EntryDefinition extends Definition {






    private List<Statement> statements;




    private List<FormalParameterDefinition> formalparameterdefinitions;


    public astm_gastm_EntryDefinition(
    ) {
        super(
        );
        this.statements = new ArrayList<>();
        this.formalparameterdefinitions = new ArrayList<>();
    }

    public astm_gastm_EntryDefinition(
        ArrayList<Statement> statements,        ArrayList<FormalParameterDefinition> formalparameterdefinitions    ) {
        this.statements = statements;
        this.formalparameterdefinitions = formalparameterdefinitions;
    }


    public List<Statement> getStatements() {
        return statements;
    }

    public void addStatement(Statement statement) {
        this.statements.add(statement);
    }
    public List<FormalParameterDefinition> getFormalparameterdefinitions() {
        return formalparameterdefinitions;
    }

    public void addFormalparameterdefinition(Formalparameterdefinition formalparameterdefinition) {
        this.formalparameterdefinitions.add(formalparameterdefinition);
    }

}