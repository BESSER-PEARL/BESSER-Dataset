





import java.util.List;
import java.util.ArrayList;

public class iot2_Board  {

    private String name;
    private String type;





    private List<iot2_HWComponent> iot2_hwcomponents;




    private iot2_System iot2_system;


    public iot2_Board(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
        this.iot2_hwcomponents = new ArrayList<>();
    }

    public iot2_Board(
        String name,        String type        ArrayList<iot2_HWComponent> iot2_hwcomponents    ) {
        this.name = name;
        this.type = type;
        this.iot2_hwcomponents = iot2_hwcomponents;
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

    public List<iot2_HWComponent> getIot2_hwcomponents() {
        return iot2_hwcomponents;
    }

    public void addIot2_hwcomponent(Iot2_hwcomponent iot2_hwcomponent) {
        this.iot2_hwcomponents.add(iot2_hwcomponent);
    }
    public iot2_System getIot2_system() {
        return iot2_system;
    }

    public void setIot2_system(iot2_System iot2_system) {
        this.iot2_system = iot2_system;
    }

}