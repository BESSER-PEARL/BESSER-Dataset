





import java.util.List;
import java.util.ArrayList;

public class polybot_While extends Instruction {

    private int nb;





    private List<polybot_Instruction> polybot_instructions;


    public polybot_While(
        int nb    ) {
        super(
        );
        this.nb = nb;
        this.polybot_instructions = new ArrayList<>();
    }

    public polybot_While(
        int nb        ArrayList<polybot_Instruction> polybot_instructions    ) {
        this.nb = nb;
        this.polybot_instructions = polybot_instructions;
    }

    public int getNb() {
        return nb;
    }

    public void setNb(int nb) {
        this.nb = nb;
    }

    public List<polybot_Instruction> getPolybot_instructions() {
        return polybot_instructions;
    }

    public void addPolybot_instruction(Polybot_instruction polybot_instruction) {
        this.polybot_instructions.add(polybot_instruction);
    }

}