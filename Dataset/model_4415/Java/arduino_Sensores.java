





import java.util.List;
import java.util.ArrayList;

public class arduino_Sensores  {

    private String med;
    private String pin;





    private arduino_Bloques arduino_bloques;




    private arduino_Sketch arduino_sketch;




    private arduino_Variar arduino_variar;


    public arduino_Sensores(
        String med,        String pin    ) {
        this.med = med;
        this.pin = pin;
    }


    public String getMed() {
        return med;
    }

    public void setMed(String med) {
        this.med = med;
    }
    public String getPin() {
        return pin;
    }

    public void setPin(String pin) {
        this.pin = pin;
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
    public arduino_Variar getArduino_variar() {
        return arduino_variar;
    }

    public void setArduino_variar(arduino_Variar arduino_variar) {
        this.arduino_variar = arduino_variar;
    }

}