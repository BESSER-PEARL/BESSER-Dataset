





import java.util.List;
import java.util.ArrayList;

public class iotw_Connection  {

    private String kind;
    private String bendpoints;
    private String routerKind;
    private String label;





    private iotw_Component iotw_component;




    private iotw_StateSchema iotw_stateschema;




    private iotw_Component iotw_component;




    private iotw_StateComponent iotw_statecomponent;




    private iotw_StateComponent iotw_statecomponent;




    private iotw_StateSchema iotw_stateschema;


    public iotw_Connection(
        String kind,        String bendpoints,        String routerKind,        String label    ) {
        this.kind = kind;
        this.bendpoints = bendpoints;
        this.routerKind = routerKind;
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
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public iotw_Component getIotw_component() {
        return iotw_component;
    }

    public void setIotw_component(iotw_Component iotw_component) {
        this.iotw_component = iotw_component;
    }
    public iotw_StateSchema getIotw_stateschema() {
        return iotw_stateschema;
    }

    public void setIotw_stateschema(iotw_StateSchema iotw_stateschema) {
        this.iotw_stateschema = iotw_stateschema;
    }
    public iotw_Component getIotw_component() {
        return iotw_component;
    }

    public void setIotw_component(iotw_Component iotw_component) {
        this.iotw_component = iotw_component;
    }
    public iotw_StateComponent getIotw_statecomponent() {
        return iotw_statecomponent;
    }

    public void setIotw_statecomponent(iotw_StateComponent iotw_statecomponent) {
        this.iotw_statecomponent = iotw_statecomponent;
    }
    public iotw_StateComponent getIotw_statecomponent() {
        return iotw_statecomponent;
    }

    public void setIotw_statecomponent(iotw_StateComponent iotw_statecomponent) {
        this.iotw_statecomponent = iotw_statecomponent;
    }
    public iotw_StateSchema getIotw_stateschema() {
        return iotw_stateschema;
    }

    public void setIotw_stateschema(iotw_StateSchema iotw_stateschema) {
        this.iotw_stateschema = iotw_stateschema;
    }

}