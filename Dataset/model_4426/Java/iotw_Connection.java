





import java.util.List;
import java.util.ArrayList;

public class iotw_Connection  {

    private String bendpoints;
    private String routerKind;
    private String label;
    private String kind;



    public iotw_Connection(
        String bendpoints,        String routerKind,        String label,        String kind    ) {
        this.bendpoints = bendpoints;
        this.routerKind = routerKind;
        this.label = label;
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


}