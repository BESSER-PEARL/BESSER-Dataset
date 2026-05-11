





import java.util.List;
import java.util.ArrayList;

public class iot2_Board  {

    private String type;
    private String name;





    private iot2_System iot2_system;




    private List<iot2_HWComponent> iot2_hwcomponents;


    public iot2_Board(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
        this.iot2_hwcomponents = new ArrayList<>();
    }

    public iot2_Board(
        String type,        String name        ArrayList<iot2_HWComponent> iot2_hwcomponents    ) {
        this.type = type;
        this.name = name;
        this.iot2_hwcomponents = iot2_hwcomponents;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public iot2_System getIot2_system() {
        return iot2_system;
    }

    public void setIot2_system(iot2_System iot2_system) {
        this.iot2_system = iot2_system;
    }
    public List<iot2_HWComponent> getIot2_hwcomponents() {
        return iot2_hwcomponents;
    }

    public void addIot2_hwcomponent(Iot2_hwcomponent iot2_hwcomponent) {
        this.iot2_hwcomponents.add(iot2_hwcomponent);
    }

}