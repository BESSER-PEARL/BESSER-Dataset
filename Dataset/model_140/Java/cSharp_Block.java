





import java.util.List;
import java.util.ArrayList;

public class cSharp_Block extends MaybeEmptyBlock, AddAccessorDeclaration, RemoveAccessorDeclaration {






    private cSharp_EmbeddedStatement csharp_embeddedstatement;




    private List<cSharp_Statement> csharp_statements;




    private cSharp_TryStatement csharp_trystatement;


    public cSharp_Block(
    ) {
        super(
        );
        this.csharp_statements = new ArrayList<>();
    }

    public cSharp_Block(
        ArrayList<cSharp_Statement> csharp_statements    ) {
        this.csharp_statements = csharp_statements;
    }


    public cSharp_EmbeddedStatement getCsharp_embeddedstatement() {
        return csharp_embeddedstatement;
    }

    public void setCsharp_embeddedstatement(cSharp_EmbeddedStatement csharp_embeddedstatement) {
        this.csharp_embeddedstatement = csharp_embeddedstatement;
    }
    public List<cSharp_Statement> getCsharp_statements() {
        return csharp_statements;
    }

    public void addCsharp_statement(Csharp_statement csharp_statement) {
        this.csharp_statements.add(csharp_statement);
    }
    public cSharp_TryStatement getCsharp_trystatement() {
        return csharp_trystatement;
    }

    public void setCsharp_trystatement(cSharp_TryStatement csharp_trystatement) {
        this.csharp_trystatement = csharp_trystatement;
    }

}