





import java.util.List;
import java.util.ArrayList;

public class simpleimperative_Conditional extends Statement {






    private List<simpleimperative_Statement> simpleimperative_statements;


    public simpleimperative_Conditional(
    ) {
        super(
        );
        this.simpleimperative_statements = new ArrayList<>();
    }

    public simpleimperative_Conditional(
        ArrayList<simpleimperative_Statement> simpleimperative_statements    ) {
        this.simpleimperative_statements = simpleimperative_statements;
    }


    public List<simpleimperative_Statement> getSimpleimperative_statements() {
        return simpleimperative_statements;
    }

    public void addSimpleimperative_statement(Simpleimperative_statement simpleimperative_statement) {
        this.simpleimperative_statements.add(simpleimperative_statement);
    }

}