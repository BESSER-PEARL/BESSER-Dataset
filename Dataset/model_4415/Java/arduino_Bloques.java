





import java.util.List;
import java.util.ArrayList;

public class arduino_Bloques  {






    private arduino_Bloques arduino_bloques;




    private arduino_Sketch arduino_sketch;




    private List<arduino_Instrucciones> arduino_instruccioness;


    public arduino_Bloques(
    ) {
        this.arduino_instruccioness = new ArrayList<>();
    }

    public arduino_Bloques(
        ArrayList<arduino_Instrucciones> arduino_instruccioness    ) {
        this.arduino_instruccioness = arduino_instruccioness;
    }


    public arduino_Bloques getArduino_bloques() {
        return arduino_bloques;
    }

    public void setArduino_bloques(arduino_Bloques arduino_bloques) {
        this.arduino_bloques = arduino_bloques;
    }
    public arduino_Sketch getArduino_sketch() {
        return arduino_sketch;
    }

    public void setArduino_sketch(arduino_Sketch arduino_sketch) {
        this.arduino_sketch = arduino_sketch;
    }
    public List<arduino_Instrucciones> getArduino_instruccioness() {
        return arduino_instruccioness;
    }

    public void addArduino_instrucciones(Arduino_instrucciones arduino_instrucciones) {
        this.arduino_instruccioness.add(arduino_instrucciones);
    }

}