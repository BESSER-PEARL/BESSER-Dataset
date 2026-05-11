





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwDatasheet_HwDatasheet  {

    private String name;
    private String revision;





    private List<HwGeneral_HwResource> hwgeneral_hwresources;


    public MARTE_HwDatasheet_HwDatasheet(
        String name,        String revision    ) {
        this.name = name;
        this.revision = revision;
        this.hwgeneral_hwresources = new ArrayList<>();
    }

    public MARTE_HwDatasheet_HwDatasheet(
        String name,        String revision        ArrayList<HwGeneral_HwResource> hwgeneral_hwresources    ) {
        this.name = name;
        this.revision = revision;
        this.hwgeneral_hwresources = hwgeneral_hwresources;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRevision() {
        return revision;
    }

    public void setRevision(String revision) {
        this.revision = revision;
    }

    public List<HwGeneral_HwResource> getHwgeneral_hwresources() {
        return hwgeneral_hwresources;
    }

    public void addHwgeneral_hwresource(Hwgeneral_hwresource hwgeneral_hwresource) {
        this.hwgeneral_hwresources.add(hwgeneral_hwresource);
    }

}