





import java.util.List;
import java.util.ArrayList;

public class arduino_Expression  {






    private arduino_ModuleSet arduino_moduleset;




    private arduino_If arduino_if;




    private arduino_While arduino_while;


    public arduino_Expression(
    ) {
    }



    public arduino_ModuleSet getArduino_moduleset() {
        return arduino_moduleset;
    }

    public void setArduino_moduleset(arduino_ModuleSet arduino_moduleset) {
        this.arduino_moduleset = arduino_moduleset;
    }
    public arduino_If getArduino_if() {
        return arduino_if;
    }

    public void setArduino_if(arduino_If arduino_if) {
        this.arduino_if = arduino_if;
    }
    public arduino_While getArduino_while() {
        return arduino_while;
    }

    public void setArduino_while(arduino_While arduino_while) {
        this.arduino_while = arduino_while;
    }

}