





import java.util.List;
import java.util.ArrayList;

public class smarthome_Duration  {

    private int time;
    private String precision;





    private smarthome_Rule smarthome_rule;


    public smarthome_Duration(
        int time,        String precision    ) {
        this.time = time;
        this.precision = precision;
    }


    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }
    public String getPrecision() {
        return precision;
    }

    public void setPrecision(String precision) {
        this.precision = precision;
    }

    public smarthome_Rule getSmarthome_rule() {
        return smarthome_rule;
    }

    public void setSmarthome_rule(smarthome_Rule smarthome_rule) {
        this.smarthome_rule = smarthome_rule;
    }

}