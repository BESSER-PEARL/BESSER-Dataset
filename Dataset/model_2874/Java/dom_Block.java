





import java.util.List;
import java.util.ArrayList;

public class dom_Block extends DomElement {






    private dom_OperationDefinition dom_operationdefinition;




    private List<dom_Statement> dom_statements;




    private dom_Program dom_program;


    public dom_Block(
    ) {
        super(
        );
        this.dom_statements = new ArrayList<>();
    }

    public dom_Block(
        ArrayList<dom_Statement> dom_statements    ) {
        this.dom_statements = dom_statements;
    }


    public dom_OperationDefinition getDom_operationdefinition() {
        return dom_operationdefinition;
    }

    public void setDom_operationdefinition(dom_OperationDefinition dom_operationdefinition) {
        this.dom_operationdefinition = dom_operationdefinition;
    }
    public List<dom_Statement> getDom_statements() {
        return dom_statements;
    }

    public void addDom_statement(Dom_statement dom_statement) {
        this.dom_statements.add(dom_statement);
    }
    public dom_Program getDom_program() {
        return dom_program;
    }

    public void setDom_program(dom_Program dom_program) {
        this.dom_program = dom_program;
    }

}