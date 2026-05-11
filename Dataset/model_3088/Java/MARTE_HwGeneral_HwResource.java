





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwGeneral_HwResource extends Resource {

    private String description;
    private String frequency;





    private List<HwGeneral_HwResource> hwgeneral_hwresources;


    public MARTE_HwGeneral_HwResource(
        String description,        String frequency    ) {
        super(
        );
        this.description = description;
        this.frequency = frequency;
        this.hwgeneral_hwresources = new ArrayList<>();
    }

    public MARTE_HwGeneral_HwResource(
        String description,        String frequency        ArrayList<HwGeneral_HwResource> hwgeneral_hwresources    ) {
        this.description = description;
        this.frequency = frequency;
        this.hwgeneral_hwresources = hwgeneral_hwresources;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getFrequency() {
        return frequency;
    }

    public void setFrequency(String frequency) {
        this.frequency = frequency;
    }

    public List<HwGeneral_HwResource> getHwgeneral_hwresources() {
        return hwgeneral_hwresources;
    }

    public void addHwgeneral_hwresource(Hwgeneral_hwresource hwgeneral_hwresource) {
        this.hwgeneral_hwresources.add(hwgeneral_hwresource);
    }

}