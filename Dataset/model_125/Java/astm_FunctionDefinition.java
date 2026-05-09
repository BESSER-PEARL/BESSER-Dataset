





import java.util.List;
import java.util.ArrayList;

public class astm_FunctionDefinition extends Definition {






    private FunctionScope functionscope;




    private TypeReference typereference;


    public astm_FunctionDefinition(
    ) {
        super(
        );
    }



    public FunctionScope getFunctionscope() {
        return functionscope;
    }

    public void setFunctionscope(FunctionScope functionscope) {
        this.functionscope = functionscope;
    }
    public TypeReference getTypereference() {
        return typereference;
    }

    public void setTypereference(TypeReference typereference) {
        this.typereference = typereference;
    }

}