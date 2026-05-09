





import java.util.List;
import java.util.ArrayList;

public class gastm_FunctionDefinition extends Definition {






    private gastm_FunctionMemberAttributes gastm_functionmemberattributes;




    private List<gastm_Statement> gastm_statements;




    private gastm_FunctionScope gastm_functionscope;




    private gastm_TypeReference gastm_typereference;


    public gastm_FunctionDefinition(
    ) {
        super(
        );
        this.gastm_statements = new ArrayList<>();
    }

    public gastm_FunctionDefinition(
        ArrayList<gastm_Statement> gastm_statements    ) {
        this.gastm_statements = gastm_statements;
    }


    public gastm_FunctionMemberAttributes getGastm_functionmemberattributes() {
        return gastm_functionmemberattributes;
    }

    public void setGastm_functionmemberattributes(gastm_FunctionMemberAttributes gastm_functionmemberattributes) {
        this.gastm_functionmemberattributes = gastm_functionmemberattributes;
    }
    public List<gastm_Statement> getGastm_statements() {
        return gastm_statements;
    }

    public void addGastm_statement(Gastm_statement gastm_statement) {
        this.gastm_statements.add(gastm_statement);
    }
    public gastm_FunctionScope getGastm_functionscope() {
        return gastm_functionscope;
    }

    public void setGastm_functionscope(gastm_FunctionScope gastm_functionscope) {
        this.gastm_functionscope = gastm_functionscope;
    }
    public gastm_TypeReference getGastm_typereference() {
        return gastm_typereference;
    }

    public void setGastm_typereference(gastm_TypeReference gastm_typereference) {
        this.gastm_typereference = gastm_typereference;
    }

}