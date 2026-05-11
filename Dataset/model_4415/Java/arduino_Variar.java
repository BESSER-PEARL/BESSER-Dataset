





import java.util.List;
import java.util.ArrayList;

public class arduino_Variar extends Instrucciones {

    private String pwm;



    public arduino_Variar(
        String pwm    ) {
        super(
        );
        this.pwm = pwm;
    }


    public String getPwm() {
        return pwm;
    }

    public void setPwm(String pwm) {
        this.pwm = pwm;
    }


}