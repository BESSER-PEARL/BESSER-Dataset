





import java.util.List;
import java.util.ArrayList;

public class arduino_Actuadores  {

    private String pin;





    private arduino_Instrucciones arduino_instrucciones;




    private arduino_Sensores arduino_sensores;




    private arduino_Bloques arduino_bloques;




    private arduino_Sketch arduino_sketch;




    private arduino_Bloques arduino_bloques;


    public arduino_Actuadores(
        String pin    ) {
        this.pin = pin;
    }


    public String getPin() {
        return pin;
    }

    public void setPin(String pin) {
        this.pin = pin;
    }

    public arduino_Instrucciones getArduino_instrucciones() {
        return arduino_instrucciones;
    }

    public void setArduino_instrucciones(arduino_Instrucciones arduino_instrucciones) {
        this.arduino_instrucciones = arduino_instrucciones;
    }
    public arduino_Sensores getArduino_sensores() {
        return arduino_sensores;
    }

    public void setArduino_sensores(arduino_Sensores arduino_sensores) {
        this.arduino_sensores = arduino_sensores;
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
    public arduino_Bloques getArduino_bloques() {
        return arduino_bloques;
    }

    public void setArduino_bloques(arduino_Bloques arduino_bloques) {
        this.arduino_bloques = arduino_bloques;
    }

}