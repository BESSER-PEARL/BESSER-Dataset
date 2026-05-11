





import java.util.List;
import java.util.ArrayList;

public class ArduinoMetamodel_Digital extends Pin {

    private String ID;





    private ArduinoMetamodel_ArduinoBoardUNO arduinometamodel_arduinoboarduno;


    public ArduinoMetamodel_Digital(
        String ID    ) {
        super(
        );
        this.ID = ID;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public ArduinoMetamodel_ArduinoBoardUNO getArduinometamodel_arduinoboarduno() {
        return arduinometamodel_arduinoboarduno;
    }

    public void setArduinometamodel_arduinoboarduno(ArduinoMetamodel_ArduinoBoardUNO arduinometamodel_arduinoboarduno) {
        this.arduinometamodel_arduinoboarduno = arduinometamodel_arduinoboarduno;
    }

}