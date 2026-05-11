





import java.util.List;
import java.util.ArrayList;

public class iot_System  {

    private String name;





    private List<iot_HWComp> iot_hwcomps;


    public iot_System(
        String name    ) {
        this.name = name;
        this.iot_hwcomps = new ArrayList<>();
    }

    public iot_System(
        String name        ArrayList<iot_HWComp> iot_hwcomps    ) {
        this.name = name;
        this.iot_hwcomps = iot_hwcomps;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<iot_HWComp> getIot_hwcomps() {
        return iot_hwcomps;
    }

    public void addIot_hwcomp(Iot_hwcomp iot_hwcomp) {
        this.iot_hwcomps.add(iot_hwcomp);
    }

}