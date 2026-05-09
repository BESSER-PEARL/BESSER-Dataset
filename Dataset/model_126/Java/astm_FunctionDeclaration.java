





import java.util.List;
import java.util.ArrayList;

public class astm_FunctionDeclaration extends Declaration {






    private astm_FunctionMemberAttributes astm_functionmemberattributes;




    private astm_TypeReference astm_typereference;


    public astm_FunctionDeclaration(
    ) {
        super(
        );
    }



    public astm_FunctionMemberAttributes getAstm_functionmemberattributes() {
        return astm_functionmemberattributes;
    }

    public void setAstm_functionmemberattributes(astm_FunctionMemberAttributes astm_functionmemberattributes) {
        this.astm_functionmemberattributes = astm_functionmemberattributes;
    }
    public astm_TypeReference getAstm_typereference() {
        return astm_typereference;
    }

    public void setAstm_typereference(astm_TypeReference astm_typereference) {
        this.astm_typereference = astm_typereference;
    }

}