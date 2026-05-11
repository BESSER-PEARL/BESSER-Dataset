





import java.util.List;
import java.util.ArrayList;

public class iec61131_pous_Array_Type_Declaration extends Type_Declaration {






    private Array_Type_Name array_type_name;




    private Array_Spec_Init array_spec_init;


    public iec61131_pous_Array_Type_Declaration(
    ) {
        super(
        );
    }



    public Array_Type_Name getArray_type_name() {
        return array_type_name;
    }

    public void setArray_type_name(Array_Type_Name array_type_name) {
        this.array_type_name = array_type_name;
    }
    public Array_Spec_Init getArray_spec_init() {
        return array_spec_init;
    }

    public void setArray_spec_init(Array_Spec_Init array_spec_init) {
        this.array_spec_init = array_spec_init;
    }

}