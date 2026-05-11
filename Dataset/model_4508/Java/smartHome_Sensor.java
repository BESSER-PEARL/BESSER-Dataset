





import java.util.List;
import java.util.ArrayList;

public class smartHome_Sensor  {

    private int value;
    private String name;
    private String dataFile;



    public smartHome_Sensor(
        int value,        String name,        String dataFile    ) {
        this.value = value;
        this.name = name;
        this.dataFile = dataFile;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDatafile() {
        return dataFile;
    }

    public void setDatafile(String dataFile) {
        this.dataFile = dataFile;
    }


}