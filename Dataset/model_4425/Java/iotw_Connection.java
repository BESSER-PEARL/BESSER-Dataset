





import java.util.List;
import java.util.ArrayList;

public class iotw_Connection  {

    private String label;
    private String kind;
    private String bendpoints;
    private String routerKind;





    private iotw_StateControl iotw_statecontrol;




    private iotw_StateControl iotw_statecontrol;




    private iotw_Control iotw_control;




    private iotw_Control iotw_control;


    public iotw_Connection(
        String label,        String kind,        String bendpoints,        String routerKind    ) {
        this.label = label;
        this.kind = kind;
        this.bendpoints = bendpoints;
        this.routerKind = routerKind;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getBendpoints() {
        return bendpoints;
    }

    public void setBendpoints(String bendpoints) {
        this.bendpoints = bendpoints;
    }
    public String getRouterkind() {
        return routerKind;
    }

    public void setRouterkind(String routerKind) {
        this.routerKind = routerKind;
    }

    public iotw_StateControl getIotw_statecontrol() {
        return iotw_statecontrol;
    }

    public void setIotw_statecontrol(iotw_StateControl iotw_statecontrol) {
        this.iotw_statecontrol = iotw_statecontrol;
    }
    public iotw_StateControl getIotw_statecontrol() {
        return iotw_statecontrol;
    }

    public void setIotw_statecontrol(iotw_StateControl iotw_statecontrol) {
        this.iotw_statecontrol = iotw_statecontrol;
    }
    public iotw_Control getIotw_control() {
        return iotw_control;
    }

    public void setIotw_control(iotw_Control iotw_control) {
        this.iotw_control = iotw_control;
    }
    public iotw_Control getIotw_control() {
        return iotw_control;
    }

    public void setIotw_control(iotw_Control iotw_control) {
        this.iotw_control = iotw_control;
    }

}