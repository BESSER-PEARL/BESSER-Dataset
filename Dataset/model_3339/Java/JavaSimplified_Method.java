





import java.util.List;
import java.util.ArrayList;

public class JavaSimplified_Method extends Feature {

    private String exceptions;





    private List<JavaSimplified_Parameter> javasimplified_parameters;




    private List<JavaSimplified_Statement> javasimplified_statements;




    private JavaSimplified_Type javasimplified_type;




    private JavaSimplified_JavaClass javasimplified_javaclass;


    public JavaSimplified_Method(
        String exceptions    ) {
        super(
        );
        this.exceptions = exceptions;
        this.javasimplified_parameters = new ArrayList<>();
        this.javasimplified_statements = new ArrayList<>();
    }

    public JavaSimplified_Method(
        String exceptions        ArrayList<JavaSimplified_Parameter> javasimplified_parameters,        ArrayList<JavaSimplified_Statement> javasimplified_statements    ) {
        this.exceptions = exceptions;
        this.javasimplified_parameters = javasimplified_parameters;
        this.javasimplified_statements = javasimplified_statements;
    }

    public String getExceptions() {
        return exceptions;
    }

    public void setExceptions(String exceptions) {
        this.exceptions = exceptions;
    }

    public List<JavaSimplified_Parameter> getJavasimplified_parameters() {
        return javasimplified_parameters;
    }

    public void addJavasimplified_parameter(Javasimplified_parameter javasimplified_parameter) {
        this.javasimplified_parameters.add(javasimplified_parameter);
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
    public JavaSimplified_JavaClass getJavasimplified_javaclass() {
        return javasimplified_javaclass;
    }

    public void setJavasimplified_javaclass(JavaSimplified_JavaClass javasimplified_javaclass) {
        this.javasimplified_javaclass = javasimplified_javaclass;
    }

}