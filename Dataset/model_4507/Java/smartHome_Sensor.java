





import java.util.List;
import java.util.ArrayList;

public class smartHome_Sensor  {

    private String name;
    private String dataFile;



    public smartHome_Sensor(
        String name,        String dataFile    ) {
        this.name = name;
        this.dataFile = dataFile;
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