





import java.util.List;
import java.util.ArrayList;

public class arduino_Block  {






    private arduino_If arduino_if;




    private arduino_Control arduino_control;




    private arduino_Sketch arduino_sketch;




    private List<arduino_Instruction> arduino_instructions;


    public arduino_Block(
    ) {
        this.arduino_instructions = new ArrayList<>();
    }

    public arduino_Block(
        ArrayList<arduino_Instruction> arduino_instructions    ) {
        this.arduino_instructions = arduino_instructions;
    }


    public arduino_If getArduino_if() {
        return arduino_if;
    }

    public void setArduino_if(arduino_If arduino_if) {
        this.arduino_if = arduino_if;
    }
    public arduino_Control getArduino_control() {
        return arduino_control;
    }

    public void setArduino_control(arduino_Control arduino_control) {
        this.arduino_control = arduino_control;
    }
    public arduino_Sketch getArduino_sketch() {
        return arduino_sketch;
    }

    public void setArduino_sketch(arduino_Sketch arduino_sketch) {
        this.arduino_sketch = arduino_sketch;
    }
    public List<arduino_Instruction> getArduino_instructions() {
        return arduino_instructions;
    }

    public void addArduino_instruction(Arduino_instruction arduino_instruction) {
        this.arduino_instructions.add(arduino_instruction);
    }

}