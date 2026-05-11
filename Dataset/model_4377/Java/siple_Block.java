





import java.util.List;
import java.util.ArrayList;

public class siple_Block extends Statement {






    private siple_ProcedureDeclaration siple_proceduredeclaration;




    private List<siple_Statement> siple_statements;




    private siple_ProcedureDeclaration siple_proceduredeclaration;


    public siple_Block(
    ) {
        super(
        );
        this.siple_statements = new ArrayList<>();
    }

    public siple_Block(
        ArrayList<siple_Statement> siple_statements    ) {
        this.siple_statements = siple_statements;
    }


    public siple_ProcedureDeclaration getSiple_proceduredeclaration() {
        return siple_proceduredeclaration;
    }

    public void setSiple_proceduredeclaration(siple_ProcedureDeclaration siple_proceduredeclaration) {
        this.siple_proceduredeclaration = siple_proceduredeclaration;
    }
    public List<siple_Statement> getSiple_statements() {
        return siple_statements;
    }

    public void addSiple_statement(Siple_statement siple_statement) {
        this.siple_statements.add(siple_statement);
    }
    public siple_ProcedureDeclaration getSiple_proceduredeclaration() {
        return siple_proceduredeclaration;
    }

    public void setSiple_proceduredeclaration(siple_ProcedureDeclaration siple_proceduredeclaration) {
        this.siple_proceduredeclaration = siple_proceduredeclaration;
    }

}