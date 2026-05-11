





import java.util.List;
import java.util.ArrayList;

public class arduino_Instruction  {






    private arduino_Sketch arduino_sketch;




    private arduino_Loop arduino_loop;




    private arduino_Instruction arduino_instruction;


    public arduino_Instruction(
    ) {
    }



    public arduino_Sketch getArduino_sketch() {
        return arduino_sketch;
    }

    public void setArduino_sketch(arduino_Sketch arduino_sketch) {
        this.arduino_sketch = arduino_sketch;
    }
    public arduino_Loop getArduino_loop() {
        return arduino_loop;
    }

    public void setArduino_loop(arduino_Loop arduino_loop) {
        this.arduino_loop = arduino_loop;
    }
    public arduino_Instruction getArduino_instruction() {
        return arduino_instruction;
    }

    public void setArduino_instruction(arduino_Instruction arduino_instruction) {
        this.arduino_instruction = arduino_instruction;
    }

}