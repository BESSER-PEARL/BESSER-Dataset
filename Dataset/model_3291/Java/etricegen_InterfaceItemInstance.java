





import java.util.List;
import java.util.ArrayList;

public class etricegen_InterfaceItemInstance extends InstanceBase {






    private List<etricegen_InterfaceItemInstance> etricegen_interfaceiteminstances;


    public etricegen_InterfaceItemInstance(
    ) {
        super(
        );
        this.etricegen_interfaceiteminstances = new ArrayList<>();
    }

    public etricegen_InterfaceItemInstance(
        ArrayList<etricegen_InterfaceItemInstance> etricegen_interfaceiteminstances    ) {
        this.etricegen_interfaceiteminstances = etricegen_interfaceiteminstances;
    }


    public List<etricegen_InterfaceItemInstance> getEtricegen_interfaceiteminstances() {
        return etricegen_interfaceiteminstances;
    }

    public void addEtricegen_interfaceiteminstance(Etricegen_interfaceiteminstance etricegen_interfaceiteminstance) {
        this.etricegen_interfaceiteminstances.add(etricegen_interfaceiteminstance);
    }

}