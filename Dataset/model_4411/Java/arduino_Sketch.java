





import java.util.List;
import java.util.ArrayList;

public class arduino_Sketch extends Instruction, NamedElement {






    private arduino_Hardware arduino_hardware;




    private List<arduino_Instruction> arduino_instructions;


    public arduino_Sketch(
    ) {
        super(
        );
        this.arduino_instructions = new ArrayList<>();
    }

    public arduino_Sketch(
        ArrayList<arduino_Instruction> arduino_instructions    ) {
        this.arduino_instructions = arduino_instructions;
    }


    public arduino_Hardware getArduino_hardware() {
        return arduino_hardware;
    }

    public void setArduino_hardware(arduino_Hardware arduino_hardware) {
        this.arduino_hardware = arduino_hardware;
    }
    public List<arduino_Instruction> getArduino_instructions() {
        return arduino_instructions;
    }

    public void addArduino_instruction(Arduino_instruction arduino_instruction) {
        this.arduino_instructions.add(arduino_instruction);
    }

}