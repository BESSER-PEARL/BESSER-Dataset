





import java.util.List;
import java.util.ArrayList;

public class arduino_Temperatura extends Sensores {

    private String temperatura;



    public arduino_Temperatura(
        String temperatura    ) {
        super(
        );
        this.temperatura = temperatura;
    }


    public String getTemperatura() {
        return temperatura;
    }

    public void setTemperatura(String temperatura) {
        this.temperatura = temperatura;
    }


}