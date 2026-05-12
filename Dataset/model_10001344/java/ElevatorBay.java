





import java.util.List;
import java.util.ArrayList;

public class ElevatorBay  {

    private String Elevators;
    private String UpDownButtons;
    private int BayNumber;





    private List<UpDownButton> updownbuttons;


    public ElevatorBay(
        String Elevators,        String UpDownButtons,        int BayNumber    ) {
        this.Elevators = Elevators;
        this.UpDownButtons = UpDownButtons;
        this.BayNumber = BayNumber;
        this.updownbuttons = new ArrayList<>();
    }

    public ElevatorBay(
        String Elevators,        String UpDownButtons,        int BayNumber        ArrayList<UpDownButton> updownbuttons    ) {
        this.Elevators = Elevators;
        this.UpDownButtons = UpDownButtons;
        this.BayNumber = BayNumber;
        this.updownbuttons = updownbuttons;
    }

    public String getElevators() {
        return Elevators;
    }

    public void setElevators(String Elevators) {
        this.Elevators = Elevators;
    }
    public String getUpdownbuttons() {
        return UpDownButtons;
    }

    public void setUpdownbuttons(String UpDownButtons) {
        this.UpDownButtons = UpDownButtons;
    }
    public int getBaynumber() {
        return BayNumber;
    }

    public void setBaynumber(int BayNumber) {
        this.BayNumber = BayNumber;
    }

    public List<UpDownButton> getUpdownbuttons() {
        return updownbuttons;
    }

    public void addUpdownbutton(Updownbutton updownbutton) {
        this.updownbuttons.add(updownbutton);
    }

}