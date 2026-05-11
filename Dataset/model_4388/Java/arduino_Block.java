





import java.util.List;
import java.util.ArrayList;

public class arduino_Block  {






    private List<arduino_Instruction> arduino_instructions;




    private arduino_Sketch arduino_sketch;


    public arduino_Block(
    ) {
        this.arduino_instructions = new ArrayList<>();
    }

    public arduino_Block(
        ArrayList<arduino_Instruction> arduino_instructions    ) {
        this.arduino_instructions = arduino_instructions;
    }


    public List<arduino_Instruction> getArduino_instructions() {
        return arduino_instructions;
    }

    public void addArduino_instruction(Arduino_instruction arduino_instruction) {
        this.arduino_instructions.add(arduino_instruction);
    }
    public arduino_Sketch getArduino_sketch() {
        return arduino_sketch;
    }

    public void setArduino_sketch(arduino_Sketch arduino_sketch) {
        this.arduino_sketch = arduino_sketch;
    }

}