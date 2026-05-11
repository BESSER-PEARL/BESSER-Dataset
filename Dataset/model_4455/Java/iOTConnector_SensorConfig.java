





import java.util.List;
import java.util.ArrayList;

public class iOTConnector_SensorConfig  {

    private String name;
    private String pinIn;
    private String pinOut;





    private iOTConnector_Board iotconnector_board;


    public iOTConnector_SensorConfig(
        String name,        String pinIn,        String pinOut    ) {
        this.name = name;
        this.pinIn = pinIn;
        this.pinOut = pinOut;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPinin() {
        return pinIn;
    }

    public void setPinin(String pinIn) {
        this.pinIn = pinIn;
    }
    public String getPinout() {
        return pinOut;
    }

    public void setPinout(String pinOut) {
        this.pinOut = pinOut;
    }

    public iOTConnector_Board getIotconnector_board() {
        return iotconnector_board;
    }

    public void setIotconnector_board(iOTConnector_Board iotconnector_board) {
        this.iotconnector_board = iotconnector_board;
    }

}