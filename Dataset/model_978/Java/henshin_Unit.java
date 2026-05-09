





import java.util.List;
import java.util.ArrayList;

public class henshin_Unit extends NamedElement {

    private boolean activated;





    private henshin_Parameter henshin_parameter;




    private List<henshin_Parameter> henshin_parameters;




    private henshin_Module henshin_module;


    public henshin_Unit(
        boolean activated    ) {
        super(
        );
        this.activated = activated;
        this.henshin_parameters = new ArrayList<>();
    }

    public henshin_Unit(
        boolean activated        ArrayList<henshin_Parameter> henshin_parameters    ) {
        this.activated = activated;
        this.henshin_parameters = henshin_parameters;
    }

    public boolean getActivated() {
        return activated;
    }

    public void setActivated(boolean activated) {
        this.activated = activated;
    }

    public henshin_Parameter getHenshin_parameter() {
        return henshin_parameter;
    }

    public void setHenshin_parameter(henshin_Parameter henshin_parameter) {
        this.henshin_parameter = henshin_parameter;
    }
    public List<henshin_Parameter> getHenshin_parameters() {
        return henshin_parameters;
    }

    public void addHenshin_parameter(Henshin_parameter henshin_parameter) {
        this.henshin_parameters.add(henshin_parameter);
    }
    public henshin_Module getHenshin_module() {
        return henshin_module;
    }

    public void setHenshin_module(henshin_Module henshin_module) {
        this.henshin_module = henshin_module;
    }

}