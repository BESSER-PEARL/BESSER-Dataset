





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwDiagram_HwBlockDiagram  {

    private String name;





    private List<HwGeneral_HwResource> hwgeneral_hwresources;


    public MARTE_HwDiagram_HwBlockDiagram(
        String name    ) {
        this.name = name;
        this.hwgeneral_hwresources = new ArrayList<>();
    }

    public MARTE_HwDiagram_HwBlockDiagram(
        String name        ArrayList<HwGeneral_HwResource> hwgeneral_hwresources    ) {
        this.name = name;
        this.hwgeneral_hwresources = hwgeneral_hwresources;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<HwGeneral_HwResource> getHwgeneral_hwresources() {
        return hwgeneral_hwresources;
    }

    public void addHwgeneral_hwresource(Hwgeneral_hwresource hwgeneral_hwresource) {
        this.hwgeneral_hwresources.add(hwgeneral_hwresource);
    }

}