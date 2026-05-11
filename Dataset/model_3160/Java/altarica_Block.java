





import java.util.List;
import java.util.ArrayList;

public class altarica_Block extends Instruction {






    private List<altarica_Instruction> altarica_instructions;


    public altarica_Block(
    ) {
        super(
        );
        this.altarica_instructions = new ArrayList<>();
    }

    public altarica_Block(
        ArrayList<altarica_Instruction> altarica_instructions    ) {
        this.altarica_instructions = altarica_instructions;
    }


    public List<altarica_Instruction> getAltarica_instructions() {
        return altarica_instructions;
    }

    public void addAltarica_instruction(Altarica_instruction altarica_instruction) {
        this.altarica_instructions.add(altarica_instruction);
    }

}