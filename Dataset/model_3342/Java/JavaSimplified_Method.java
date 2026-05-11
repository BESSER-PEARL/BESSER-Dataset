





import java.util.List;
import java.util.ArrayList;

public class JavaSimplified_Method extends NamedElement, CommentedElement, StringElement {

    private String exceptions;





    private List<JavaSimplified_Statement> javasimplified_statements;




    private JavaSimplified_Type javasimplified_type;




    private List<JavaSimplified_Parameter> javasimplified_parameters;


    public JavaSimplified_Method(
        String exceptions    ) {
        super(
        );
        this.exceptions = exceptions;
        this.javasimplified_statements = new ArrayList<>();
        this.javasimplified_parameters = new ArrayList<>();
    }

    public JavaSimplified_Method(
        String exceptions        ArrayList<JavaSimplified_Statement> javasimplified_statements,        ArrayList<JavaSimplified_Parameter> javasimplified_parameters    ) {
        this.exceptions = exceptions;
        this.javasimplified_statements = javasimplified_statements;
        this.javasimplified_parameters = javasimplified_parameters;
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
    public JavaSimplified_Type getJavasimplified_type() {
        return javasimplified_type;
    }

    public void setJavasimplified_type(JavaSimplified_Type javasimplified_type) {
        this.javasimplified_type = javasimplified_type;
    }
    public List<JavaSimplified_Parameter> getJavasimplified_parameters() {
        return javasimplified_parameters;
    }

    public void addJavasimplified_parameter(Javasimplified_parameter javasimplified_parameter) {
        this.javasimplified_parameters.add(javasimplified_parameter);
    }

}