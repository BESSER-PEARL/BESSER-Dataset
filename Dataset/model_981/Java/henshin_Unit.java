





import java.util.List;
import java.util.ArrayList;

public class henshin_Unit extends NamedElement {

    private boolean activated;
    private boolean isUsed;





    private List<henshin_ParameterMapping> henshin_parametermappings;




    private henshin_Module henshin_module;


    public henshin_Unit(
        boolean activated,        boolean isUsed    ) {
        super(
        );
        this.activated = activated;
        this.isUsed = isUsed;
        this.henshin_parametermappings = new ArrayList<>();
    }

    public henshin_Unit(
        boolean activated,        boolean isUsed        ArrayList<henshin_ParameterMapping> henshin_parametermappings    ) {
        this.activated = activated;
        this.isUsed = isUsed;
        this.henshin_parametermappings = henshin_parametermappings;
    }

    public boolean getActivated() {
        return activated;
    }

    public void setActivated(boolean activated) {
        this.activated = activated;
    }
    public boolean getIsused() {
        return isUsed;
    }

    public void setIsused(boolean isUsed) {
        this.isUsed = isUsed;
    }

    public List<henshin_ParameterMapping> getHenshin_parametermappings() {
        return henshin_parametermappings;
    }

    public void addHenshin_parametermapping(Henshin_parametermapping henshin_parametermapping) {
        this.henshin_parametermappings.add(henshin_parametermapping);
    }
    public henshin_Module getHenshin_module() {
        return henshin_module;
    }

    public void setHenshin_module(henshin_Module henshin_module) {
        this.henshin_module = henshin_module;
    }

}