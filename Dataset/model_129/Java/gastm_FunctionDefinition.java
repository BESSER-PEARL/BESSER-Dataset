





import java.util.List;
import java.util.ArrayList;

public class gastm_FunctionDefinition extends Definition {






    private FunctionMemberAttributes functionmemberattributes;




    private List<TypeReference> typereferences;


    public gastm_FunctionDefinition(
    ) {
        super(
        );
        this.typereferences = new ArrayList<>();
    }

    public gastm_FunctionDefinition(
        ArrayList<TypeReference> typereferences    ) {
        this.typereferences = typereferences;
    }


    public FunctionMemberAttributes getFunctionmemberattributes() {
        return functionmemberattributes;
    }

    public void setFunctionmemberattributes(FunctionMemberAttributes functionmemberattributes) {
        this.functionmemberattributes = functionmemberattributes;
    }
    public List<TypeReference> getTypereferences() {
        return typereferences;
    }

    public void addTypereference(Typereference typereference) {
        this.typereferences.add(typereference);
    }

}