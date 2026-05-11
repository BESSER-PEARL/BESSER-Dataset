





import java.util.List;
import java.util.ArrayList;

public class rm_VariableReference  {

    private String variable;
    private int memoryCellIndex;





    private rm_Memory rm_memory;


    public rm_VariableReference(
        String variable,        int memoryCellIndex    ) {
        this.variable = variable;
        this.memoryCellIndex = memoryCellIndex;
    }


    public String getVariable() {
        return variable;
    }

    public void setVariable(String variable) {
        this.variable = variable;
    }
    public int getMemorycellindex() {
        return memoryCellIndex;
    }

    public void setMemorycellindex(int memoryCellIndex) {
        this.memoryCellIndex = memoryCellIndex;
    }

    public rm_Memory getRm_memory() {
        return rm_memory;
    }

    public void setRm_memory(rm_Memory rm_memory) {
        this.rm_memory = rm_memory;
    }

}