





import java.util.List;
import java.util.ArrayList;

public class arduino_Pin  {

    private int id;
    private int level;





    private arduino_Connector arduino_connector;


    public arduino_Pin(
        int id,        int level    ) {
        this.id = id;
        this.level = level;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }

    public arduino_Connector getArduino_connector() {
        return arduino_connector;
    }

    public void setArduino_connector(arduino_Connector arduino_connector) {
        this.arduino_connector = arduino_connector;
    }

}