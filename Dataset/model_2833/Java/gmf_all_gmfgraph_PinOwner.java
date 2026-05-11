





import java.util.List;
import java.util.ArrayList;

public class gmf_all_gmfgraph_PinOwner  {






    private List<Pin> pins;


    public gmf_all_gmfgraph_PinOwner(
    ) {
        this.pins = new ArrayList<>();
    }

    public gmf_all_gmfgraph_PinOwner(
        ArrayList<Pin> pins    ) {
        this.pins = pins;
    }


    public List<Pin> getPins() {
        return pins;
    }

    public void addPin(Pin pin) {
        this.pins.add(pin);
    }

}