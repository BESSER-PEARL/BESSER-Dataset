





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Connect  {

    private String pin;
    private String route;
    private String gate;
    private String pad;





    private eaglemodel_Connects eaglemodel_connects;


    public eaglemodel_Connect(
        String pin,        String route,        String gate,        String pad    ) {
        this.pin = pin;
        this.route = route;
        this.gate = gate;
        this.pad = pad;
    }


    public String getPin() {
        return pin;
    }

    public void setPin(String pin) {
        this.pin = pin;
    }
    public String getRoute() {
        return route;
    }

    public void setRoute(String route) {
        this.route = route;
    }
    public String getGate() {
        return gate;
    }

    public void setGate(String gate) {
        this.gate = gate;
    }
    public String getPad() {
        return pad;
    }

    public void setPad(String pad) {
        this.pad = pad;
    }

    public eaglemodel_Connects getEaglemodel_connects() {
        return eaglemodel_connects;
    }

    public void setEaglemodel_connects(eaglemodel_Connects eaglemodel_connects) {
        this.eaglemodel_connects = eaglemodel_connects;
    }

}