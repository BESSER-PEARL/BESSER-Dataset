





import java.util.List;
import java.util.ArrayList;

public class iec61131_interfaces_Structured_Var_Declaration extends Temp_Var_Declaration {






    private Structure_Type_Name structure_type_name;


    public iec61131_interfaces_Structured_Var_Declaration(
    ) {
        super(
        );
    }



    public Structure_Type_Name getStructure_type_name() {
        return structure_type_name;
    }

    public void setStructure_type_name(Structure_Type_Name structure_type_name) {
        this.structure_type_name = structure_type_name;
    }

}