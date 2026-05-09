





import java.util.List;
import java.util.ArrayList;

public class astm_FunctionDefinition extends Definition {






    private astm_FunctionMemberAttributes astm_functionmemberattributes;




    private List<astm_FormalParameterDefinition> astm_formalparameterdefinitions;




    private astm_TypeReference astm_typereference;




    private List<astm_Statement> astm_statements;


    public astm_FunctionDefinition(
    ) {
        super(
        );
        this.astm_formalparameterdefinitions = new ArrayList<>();
        this.astm_statements = new ArrayList<>();
    }

    public astm_FunctionDefinition(
        ArrayList<astm_FormalParameterDefinition> astm_formalparameterdefinitions,        ArrayList<astm_Statement> astm_statements    ) {
        this.astm_formalparameterdefinitions = astm_formalparameterdefinitions;
        this.astm_statements = astm_statements;
    }


    public astm_FunctionMemberAttributes getAstm_functionmemberattributes() {
        return astm_functionmemberattributes;
    }

    public void setAstm_functionmemberattributes(astm_FunctionMemberAttributes astm_functionmemberattributes) {
        this.astm_functionmemberattributes = astm_functionmemberattributes;
    }
    public List<astm_FormalParameterDefinition> getAstm_formalparameterdefinitions() {
        return astm_formalparameterdefinitions;
    }

    public void addAstm_formalparameterdefinition(Astm_formalparameterdefinition astm_formalparameterdefinition) {
        this.astm_formalparameterdefinitions.add(astm_formalparameterdefinition);
    }
    public astm_TypeReference getAstm_typereference() {
        return astm_typereference;
    }

    public void setAstm_typereference(astm_TypeReference astm_typereference) {
        this.astm_typereference = astm_typereference;
    }
    public List<astm_Statement> getAstm_statements() {
        return astm_statements;
    }

    public void addAstm_statement(Astm_statement astm_statement) {
        this.astm_statements.add(astm_statement);
    }

}