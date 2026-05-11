





import java.util.List;
import java.util.ArrayList;

public class mindstorms_Choreography extends Instruction {






    private List<mindstorms_Instruction> mindstorms_instructions;


    public mindstorms_Choreography(
    ) {
        super(
        );
        this.mindstorms_instructions = new ArrayList<>();
    }

    public mindstorms_Choreography(
        ArrayList<mindstorms_Instruction> mindstorms_instructions    ) {
        this.mindstorms_instructions = mindstorms_instructions;
    }


    public List<mindstorms_Instruction> getMindstorms_instructions() {
        return mindstorms_instructions;
    }

    public void addMindstorms_instruction(Mindstorms_instruction mindstorms_instruction) {
        this.mindstorms_instructions.add(mindstorms_instruction);
    }

}