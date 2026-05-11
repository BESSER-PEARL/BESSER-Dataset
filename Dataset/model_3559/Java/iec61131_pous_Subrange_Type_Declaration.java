





import java.util.List;
import java.util.ArrayList;

public class iec61131_pous_Subrange_Type_Declaration extends Single_Element_Type_Declaration {






    private Subrange_Spec_Init subrange_spec_init;




    private Subrange_Type_Name subrange_type_name;


    public iec61131_pous_Subrange_Type_Declaration(
    ) {
        super(
        );
    }



    public Subrange_Spec_Init getSubrange_spec_init() {
        return subrange_spec_init;
    }

    public void setSubrange_spec_init(Subrange_Spec_Init subrange_spec_init) {
        this.subrange_spec_init = subrange_spec_init;
    }
    public Subrange_Type_Name getSubrange_type_name() {
        return subrange_type_name;
    }

    public void setSubrange_type_name(Subrange_Type_Name subrange_type_name) {
        this.subrange_type_name = subrange_type_name;
    }

}