





import java.util.List;
import java.util.ArrayList;

public class JavaSimplified_Method extends StringElement, CommentedElement, NamedElement {

    private String exceptions;





    private JavaSimplified_Type javasimplified_type;




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

    public JavaSimplified_Type getJavasimplified_type() {
        return javasimplified_type;
    }

    public void setJavasimplified_type(JavaSimplified_Type javasimplified_type) {
        this.javasimplified_type = javasimplified_type;
    }
    public List<JavaSimplified_Statement> getJavasimplified_statements() {
        return javasimplified_statements;
    }

    public void addJavasimplified_statement(Javasimplified_statement javasimplified_statement) {
        this.javasimplified_statements.add(javasimplified_statement);
    }

}