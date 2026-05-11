





import java.util.List;
import java.util.ArrayList;

public class arduino_Control extends Instruction {






    private List<arduino_Instruction> arduino_instructions;


    public arduino_Control(
    ) {
        super(
        );
        this.arduino_instructions = new ArrayList<>();
    }

    public arduino_Control(
        ArrayList<arduino_Instruction> arduino_instructions    ) {
        this.arduino_instructions = arduino_instructions;
    }


    public List<arduino_Instruction> getArduino_instructions() {
        return arduino_instructions;
    }

    public void addArduino_instruction(Arduino_instruction arduino_instruction) {
        this.arduino_instructions.add(arduino_instruction);
    }

}