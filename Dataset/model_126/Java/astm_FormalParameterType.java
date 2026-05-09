





import java.util.List;
import java.util.ArrayList;

public class astm_FormalParameterType extends DataType {






    private astm_FunctionType astm_functiontype;




    private astm_TypeReference astm_typereference;


    public astm_FormalParameterType(
    ) {
        super(
        );
    }



    public astm_FunctionType getAstm_functiontype() {
        return astm_functiontype;
    }

    public void setAstm_functiontype(astm_FunctionType astm_functiontype) {
        this.astm_functiontype = astm_functiontype;
    }
    public astm_TypeReference getAstm_typereference() {
        return astm_typereference;
    }

    public void setAstm_typereference(astm_TypeReference astm_typereference) {
        this.astm_typereference = astm_typereference;
    }

}