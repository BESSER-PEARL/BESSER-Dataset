





import java.util.List;
import java.util.ArrayList;

public class ArduinoCard_BlockInteraction  {

    private boolean isHigh;
    private String name;





    private ArduinoCard_Card arduinocard_card;


    public ArduinoCard_BlockInteraction(
        boolean isHigh,        String name    ) {
        this.isHigh = isHigh;
        this.name = name;
    }


    public boolean getIshigh() {
        return isHigh;
    }

    public void setIshigh(boolean isHigh) {
        this.isHigh = isHigh;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ArduinoCard_Card getArduinocard_card() {
        return arduinocard_card;
    }

    public void setArduinocard_card(ArduinoCard_Card arduinocard_card) {
        this.arduinocard_card = arduinocard_card;
    }

}