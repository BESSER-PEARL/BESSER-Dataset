





import java.util.List;
import java.util.ArrayList;

public class arduino_Function  {

    private String name;





    private arduino_FunctionCall arduino_functioncall;




    private List<arduino_Instruction> arduino_instructions;




    private arduino_Sketch arduino_sketch;


    public arduino_Function(
        String name    ) {
        this.name = name;
        this.arduino_instructions = new ArrayList<>();
    }

    public arduino_Function(
        String name        ArrayList<arduino_Instruction> arduino_instructions    ) {
        this.name = name;
        this.arduino_instructions = arduino_instructions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public arduino_FunctionCall getArduino_functioncall() {
        return arduino_functioncall;
    }

    public void setArduino_functioncall(arduino_FunctionCall arduino_functioncall) {
        this.arduino_functioncall = arduino_functioncall;
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