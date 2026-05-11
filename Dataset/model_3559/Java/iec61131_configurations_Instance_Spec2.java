





import java.util.List;
import java.util.ArrayList;

public class iec61131_configurations_Instance_Spec2 extends Instance_Specific_Init {






    private Structure_Initialization structure_initialization;




    private Variable_Name variable_name;




    private Function_Block_Type_Name function_block_type_name;




    private Assignment_Symbol assignment_symbol;


    public iec61131_configurations_Instance_Spec2(
    ) {
        super(
        );
    }



    public Structure_Initialization getStructure_initialization() {
        return structure_initialization;
    }

    public void setStructure_initialization(Structure_Initialization structure_initialization) {
        this.structure_initialization = structure_initialization;
    }
    public Variable_Name getVariable_name() {
        return variable_name;
    }

    public void setVariable_name(Variable_Name variable_name) {
        this.variable_name = variable_name;
    }
    public Function_Block_Type_Name getFunction_block_type_name() {
        return function_block_type_name;
    }

    public void setFunction_block_type_name(Function_Block_Type_Name function_block_type_name) {
        this.function_block_type_name = function_block_type_name;
    }
    public Assignment_Symbol getAssignment_symbol() {
        return assignment_symbol;
    }

    public void setAssignment_symbol(Assignment_Symbol assignment_symbol) {
        this.assignment_symbol = assignment_symbol;
    }

}