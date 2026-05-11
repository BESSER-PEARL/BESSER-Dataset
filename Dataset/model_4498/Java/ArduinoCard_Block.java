





import java.util.List;
import java.util.ArrayList;

public class ArduinoCard_Block  {

    private String name;
    private String isAnalogic;
    private int pinNumber;





    private ArduinoCard_Card arduinocard_card;


    public ArduinoCard_Block(
        String name,        String isAnalogic,        int pinNumber    ) {
        this.name = name;
        this.isAnalogic = isAnalogic;
        this.pinNumber = pinNumber;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIsanalogic() {
        return isAnalogic;
    }

    public void setIsanalogic(String isAnalogic) {
        this.isAnalogic = isAnalogic;
    }
    public int getPinnumber() {
        return pinNumber;
    }

    public void setPinnumber(int pinNumber) {
        this.pinNumber = pinNumber;
    }

    public ArduinoCard_Card getArduinocard_card() {
        return arduinocard_card;
    }

    public void setArduinocard_card(ArduinoCard_Card arduinocard_card) {
        this.arduinocard_card = arduinocard_card;
    }

}