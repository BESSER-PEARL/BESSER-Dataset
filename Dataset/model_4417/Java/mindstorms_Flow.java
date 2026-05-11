





import java.util.List;
import java.util.ArrayList;

public class mindstorms_Flow extends Instruction {






    private List<mindstorms_Instruction> mindstorms_instructions;




    private mindstorms_Instruction mindstorms_instruction;


    public mindstorms_Flow(
    ) {
        super(
        );
        this.mindstorms_instructions = new ArrayList<>();
    }

    public mindstorms_Flow(
        ArrayList<mindstorms_Instruction> mindstorms_instructions    ) {
        this.mindstorms_instructions = mindstorms_instructions;
    }


    public List<mindstorms_Instruction> getMindstorms_instructions() {
        return mindstorms_instructions;
    }

    public void addMindstorms_instruction(Mindstorms_instruction mindstorms_instruction) {
        this.mindstorms_instructions.add(mindstorms_instruction);
    }
    public mindstorms_Instruction getMindstorms_instruction() {
        return mindstorms_instruction;
    }

    public void setMindstorms_instruction(mindstorms_Instruction mindstorms_instruction) {
        this.mindstorms_instruction = mindstorms_instruction;
    }

}