





import java.util.List;
import java.util.ArrayList;

public class iec61131_interfaces_Var_Name_Decl extends Simple_Spec_Init {






    private Constant constant;




    private Structure_Initialization structure_initialization;


    public iec61131_interfaces_Var_Name_Decl(
    ) {
        super(
        );
    }



    public Constant getConstant() {
        return constant;
    }

    public void setConstant(Constant constant) {
        this.constant = constant;
    }
    public Structure_Initialization getStructure_initialization() {
        return structure_initialization;
    }

    public void setStructure_initialization(Structure_Initialization structure_initialization) {
        this.structure_initialization = structure_initialization;
    }

}