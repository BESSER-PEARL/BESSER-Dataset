





import java.util.List;
import java.util.ArrayList;

public class eol_Block extends EolElement {






    private List<eol_Statement> eol_statements;




    private eol_Program eol_program;


    public eol_Block(
    ) {
        super(
        );
        this.eol_statements = new ArrayList<>();
    }

    public eol_Block(
        ArrayList<eol_Statement> eol_statements    ) {
        this.eol_statements = eol_statements;
    }


    public List<eol_Statement> getEol_statements() {
        return eol_statements;
    }

    public void addEol_statement(Eol_statement eol_statement) {
        this.eol_statements.add(eol_statement);
    }
    public eol_Program getEol_program() {
        return eol_program;
    }

    public void setEol_program(eol_Program eol_program) {
        this.eol_program = eol_program;
    }

}