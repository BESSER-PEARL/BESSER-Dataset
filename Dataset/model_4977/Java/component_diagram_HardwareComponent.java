





import java.util.List;
import java.util.ArrayList;

public class component_diagram_HardwareComponent extends ComponentType {

    private String powerSupply;



    public component_diagram_HardwareComponent(
        String powerSupply    ) {
        super(
        );
        this.powerSupply = powerSupply;
    }


    public String getPowersupply() {
        return powerSupply;
    }

    public void setPowersupply(String powerSupply) {
        this.powerSupply = powerSupply;
    }


}