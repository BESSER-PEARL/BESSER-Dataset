





import java.util.List;
import java.util.ArrayList;

public class iot_Sensor extends Hardware {

    private String script;



    public iot_Sensor(
        String script    ) {
        super(
        );
        this.script = script;
    }


    public String getScript() {
        return script;
    }

    public void setScript(String script) {
        this.script = script;
    }


}