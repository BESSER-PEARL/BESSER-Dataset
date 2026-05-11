





import java.util.List;
import java.util.ArrayList;

public class arduino_Servo extends Actuadores {

    private String libreria;
    private String angulo;



    public arduino_Servo(
        String libreria,        String angulo    ) {
        super(
        );
        this.libreria = libreria;
        this.angulo = angulo;
    }


    public String getLibreria() {
        return libreria;
    }

    public void setLibreria(String libreria) {
        this.libreria = libreria;
    }
    public String getAngulo() {
        return angulo;
    }

    public void setAngulo(String angulo) {
        this.angulo = angulo;
    }


}