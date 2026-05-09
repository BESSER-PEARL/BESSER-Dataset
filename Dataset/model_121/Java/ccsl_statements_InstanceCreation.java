





import java.util.List;
import java.util.ArrayList;

public class ccsl_statements_InstanceCreation extends Statement {

    private String argsKind;





    private datatype_ObjectType datatype_objecttype;




    private method_Constructor method_constructor;




    private List<statements_Statement> statements_statements;


    public ccsl_statements_InstanceCreation(
        String argsKind    ) {
        super(
        );
        this.argsKind = argsKind;
        this.statements_statements = new ArrayList<>();
    }

    public ccsl_statements_InstanceCreation(
        String argsKind        ArrayList<statements_Statement> statements_statements    ) {
        this.argsKind = argsKind;
        this.statements_statements = statements_statements;
    }

    public String getArgskind() {
        return argsKind;
    }

    public void setArgskind(String argsKind) {
        this.argsKind = argsKind;
    }

    public datatype_ObjectType getDatatype_objecttype() {
        return datatype_objecttype;
    }

    public void setDatatype_objecttype(datatype_ObjectType datatype_objecttype) {
        this.datatype_objecttype = datatype_objecttype;
    }
    public method_Constructor getMethod_constructor() {
        return method_constructor;
    }

    public void setMethod_constructor(method_Constructor method_constructor) {
        this.method_constructor = method_constructor;
    }
    public List<statements_Statement> getStatements_statements() {
        return statements_statements;
    }

    public void addStatements_statement(Statements_statement statements_statement) {
        this.statements_statements.add(statements_statement);
    }

}