





import java.util.List;
import java.util.ArrayList;

public class timedAutomata_declarations_IterationStatement extends Statement {






    private Identifier identifier;




    private types_Type types_type;




    private declarations_Statement declarations_statement;


    public timedAutomata_declarations_IterationStatement(
    ) {
        super(
        );
    }



    public Identifier getIdentifier() {
        return identifier;
    }

    public void setIdentifier(Identifier identifier) {
        this.identifier = identifier;
    }
    public types_Type getTypes_type() {
        return types_type;
    }

    public void setTypes_type(types_Type types_type) {
        this.types_type = types_type;
    }
    public declarations_Statement getDeclarations_statement() {
        return declarations_statement;
    }

    public void setDeclarations_statement(declarations_Statement declarations_statement) {
        this.declarations_statement = declarations_statement;
    }

}