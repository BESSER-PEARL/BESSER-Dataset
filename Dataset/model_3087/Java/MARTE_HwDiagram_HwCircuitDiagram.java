





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwDiagram_HwCircuitDiagram  {

    private String name;





    private List<HwPackage_HwWire> hwpackage_hwwires;


    public MARTE_HwDiagram_HwCircuitDiagram(
        String name    ) {
        this.name = name;
        this.hwpackage_hwwires = new ArrayList<>();
    }

    public MARTE_HwDiagram_HwCircuitDiagram(
        String name        ArrayList<HwPackage_HwWire> hwpackage_hwwires    ) {
        this.name = name;
        this.hwpackage_hwwires = hwpackage_hwwires;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<HwPackage_HwWire> getHwpackage_hwwires() {
        return hwpackage_hwwires;
    }

    public void addHwpackage_hwwire(Hwpackage_hwwire hwpackage_hwwire) {
        this.hwpackage_hwwires.add(hwpackage_hwwire);
    }

}