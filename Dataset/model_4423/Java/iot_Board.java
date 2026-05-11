





import java.util.List;
import java.util.ArrayList;

public class iot_Board  {

    private String name;
    private String type;





    private List<iot_HWComp> iot_hwcomps;




    private iot_System iot_system;


    public iot_Board(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
        this.iot_hwcomps = new ArrayList<>();
    }

    public iot_Board(
        String name,        String type        ArrayList<iot_HWComp> iot_hwcomps    ) {
        this.name = name;
        this.type = type;
        this.iot_hwcomps = iot_hwcomps;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<iot_HWComp> getIot_hwcomps() {
        return iot_hwcomps;
    }

    public void addIot_hwcomp(Iot_hwcomp iot_hwcomp) {
        this.iot_hwcomps.add(iot_hwcomp);
    }
    public iot_System getIot_system() {
        return iot_system;
    }

    public void setIot_system(iot_System iot_system) {
        this.iot_system = iot_system;
    }

}