





import java.util.List;
import java.util.ArrayList;

public class kmLogo_Block extends Instruction {






    private List<kmLogo_Instruction> kmlogo_instructions;


    public kmLogo_Block(
    ) {
        super(
        );
        this.kmlogo_instructions = new ArrayList<>();
    }

    public kmLogo_Block(
        ArrayList<kmLogo_Instruction> kmlogo_instructions    ) {
        this.kmlogo_instructions = kmlogo_instructions;
    }


    public List<kmLogo_Instruction> getKmlogo_instructions() {
        return kmlogo_instructions;
    }

    public void addKmlogo_instruction(Kmlogo_instruction kmlogo_instruction) {
        this.kmlogo_instructions.add(kmlogo_instruction);
    }

}