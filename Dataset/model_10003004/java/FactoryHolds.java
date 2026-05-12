





import java.util.List;
import java.util.ArrayList;

public class FactoryHolds  {

    private float Time;
    private String Conveyor1;
    private String Alarm;
    private String Control_panel;
    private String Conveyor2;





    private Gateway gateway;


    public FactoryHolds(
        float Time,        String Conveyor1,        String Alarm,        String Control_panel,        String Conveyor2    ) {
        this.Time = Time;
        this.Conveyor1 = Conveyor1;
        this.Alarm = Alarm;
        this.Control_panel = Control_panel;
        this.Conveyor2 = Conveyor2;
    }


    public float getTime() {
        return Time;
    }

    public void setTime(float Time) {
        this.Time = Time;
    }
    public String getConveyor1() {
        return Conveyor1;
    }

    public void setConveyor1(String Conveyor1) {
        this.Conveyor1 = Conveyor1;
    }
    public String getAlarm() {
        return Alarm;
    }

    public void setAlarm(String Alarm) {
        this.Alarm = Alarm;
    }
    public String getControl_panel() {
        return Control_panel;
    }

    public void setControl_panel(String Control_panel) {
        this.Control_panel = Control_panel;
    }
    public String getConveyor2() {
        return Conveyor2;
    }

    public void setConveyor2(String Conveyor2) {
        this.Conveyor2 = Conveyor2;
    }

    public Gateway getGateway() {
        return gateway;
    }

    public void setGateway(Gateway gateway) {
        this.gateway = gateway;
    }

}