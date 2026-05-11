





import java.util.List;
import java.util.ArrayList;

public class iec61131_il_Il_Operand_List  {






    private List<Il_Operand> il_operands;


    public iec61131_il_Il_Operand_List(
    ) {
        this.il_operands = new ArrayList<>();
    }

    public iec61131_il_Il_Operand_List(
        ArrayList<Il_Operand> il_operands    ) {
        this.il_operands = il_operands;
    }


    public List<Il_Operand> getIl_operands() {
        return il_operands;
    }

    public void addIl_operand(Il_operand il_operand) {
        this.il_operands.add(il_operand);
    }

}