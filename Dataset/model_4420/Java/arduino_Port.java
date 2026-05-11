





import java.util.List;
import java.util.ArrayList;

public class arduino_Port  {

    private String report;
    private String map;
    private int channel;
    private String name;



    public arduino_Port(
        String report,        String map,        int channel,        String name    ) {
        this.report = report;
        this.map = map;
        this.channel = channel;
        this.name = name;
    }


    public String getReport() {
        return report;
    }

    public void setReport(String report) {
        this.report = report;
    }
    public String getMap() {
        return map;
    }

    public void setMap(String map) {
        this.map = map;
    }
    public int getChannel() {
        return channel;
    }

    public void setChannel(int channel) {
        this.channel = channel;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}