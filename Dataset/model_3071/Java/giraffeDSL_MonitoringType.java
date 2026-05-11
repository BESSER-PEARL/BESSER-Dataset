





import java.util.List;
import java.util.ArrayList;

public class giraffeDSL_MonitoringType  {

    private String type;
    private String many;
    private String name;





    private giraffeDSL_Monitor giraffedsl_monitor;


    public giraffeDSL_MonitoringType(
        String type,        String many,        String name    ) {
        this.type = type;
        this.many = many;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getMany() {
        return many;
    }

    public void setMany(String many) {
        this.many = many;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public giraffeDSL_Monitor getGiraffedsl_monitor() {
        return giraffedsl_monitor;
    }

    public void setGiraffedsl_monitor(giraffeDSL_Monitor giraffedsl_monitor) {
        this.giraffedsl_monitor = giraffedsl_monitor;
    }

}