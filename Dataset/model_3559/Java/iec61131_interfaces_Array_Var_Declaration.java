





import java.util.List;
import java.util.ArrayList;

public class iec61131_interfaces_Array_Var_Declaration extends Temp_Var_Declaration {






    private Array_Specification array_specification;


    public iec61131_interfaces_Array_Var_Declaration(
    ) {
        super(
        );
    }



    public Array_Specification getArray_specification() {
        return array_specification;
    }

    public void setArray_specification(Array_Specification array_specification) {
        this.array_specification = array_specification;
    }

}