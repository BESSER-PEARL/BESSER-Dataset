





import java.util.List;
import java.util.ArrayList;

public class JavaSimplified_Method extends CommentedElement, StringElement, NamedElement {

    private String exceptions;





    private List<JavaSimplified_Statement> javasimplified_statements;


    public JavaSimplified_Method(
        String exceptions    ) {
        super(
        );
        this.exceptions = exceptions;
        this.javasimplified_statements = new ArrayList<>();
    }

    public JavaSimplified_Method(
        String exceptions        ArrayList<JavaSimplified_Statement> javasimplified_statements    ) {
        this.exceptions = exceptions;
        this.javasimplified_statements = javasimplified_statements;
    }

    public String getExceptions() {
        return exceptions;
    }

    public void setExceptions(String exceptions) {
        this.exceptions = exceptions;
    }

    public List<JavaSimplified_Statement> getJavasimplified_statements() {
        return javasimplified_statements;
    }

    public void addJavasimplified_statement(Javasimplified_statement javasimplified_statement) {
        this.javasimplified_statements.add(javasimplified_statement);
    }

}