





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_PinOwner  {






    private List<gmfgraph_Pin> gmfgraph_pins;


    public gmfgraph_PinOwner(
    ) {
        this.gmfgraph_pins = new ArrayList<>();
    }

    public gmfgraph_PinOwner(
        ArrayList<gmfgraph_Pin> gmfgraph_pins    ) {
        this.gmfgraph_pins = gmfgraph_pins;
    }


    public List<gmfgraph_Pin> getGmfgraph_pins() {
        return gmfgraph_pins;
    }

    public void addGmfgraph_pin(Gmfgraph_pin gmfgraph_pin) {
        this.gmfgraph_pins.add(gmfgraph_pin);
    }

}