





import java.util.List;
import java.util.ArrayList;

public class camel_metric_Sensor  {

    private String name;
    private boolean isPush;
    private String configuration;



    public camel_metric_Sensor(
        String name,        boolean isPush,        String configuration    ) {
        this.name = name;
        this.isPush = isPush;
        this.configuration = configuration;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIspush() {
        return isPush;
    }

    public void setIspush(boolean isPush) {
        this.isPush = isPush;
    }
    public String getConfiguration() {
        return configuration;
    }

    public void setConfiguration(String configuration) {
        this.configuration = configuration;
    }


}