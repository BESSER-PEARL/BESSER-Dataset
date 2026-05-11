





import java.util.List;
import java.util.ArrayList;

public class etricegen_StructureInstance extends AbstractInstance {






    private List<etricegen_SPPInstance> etricegen_sppinstances;




    private List<etricegen_AbstractInstance> etricegen_abstractinstances;




    private List<etricegen_InterfaceItemInstance> etricegen_interfaceiteminstances;


    public etricegen_StructureInstance(
    ) {
        super(
        );
        this.etricegen_sppinstances = new ArrayList<>();
        this.etricegen_abstractinstances = new ArrayList<>();
        this.etricegen_interfaceiteminstances = new ArrayList<>();
    }

    public etricegen_StructureInstance(
        ArrayList<etricegen_SPPInstance> etricegen_sppinstances,        ArrayList<etricegen_AbstractInstance> etricegen_abstractinstances,        ArrayList<etricegen_InterfaceItemInstance> etricegen_interfaceiteminstances    ) {
        this.etricegen_sppinstances = etricegen_sppinstances;
        this.etricegen_abstractinstances = etricegen_abstractinstances;
        this.etricegen_interfaceiteminstances = etricegen_interfaceiteminstances;
    }


    public List<etricegen_SPPInstance> getEtricegen_sppinstances() {
        return etricegen_sppinstances;
    }

    public void addEtricegen_sppinstance(Etricegen_sppinstance etricegen_sppinstance) {
        this.etricegen_sppinstances.add(etricegen_sppinstance);
    }
    public List<etricegen_AbstractInstance> getEtricegen_abstractinstances() {
        return etricegen_abstractinstances;
    }

    public void addEtricegen_abstractinstance(Etricegen_abstractinstance etricegen_abstractinstance) {
        this.etricegen_abstractinstances.add(etricegen_abstractinstance);
    }
    public List<etricegen_InterfaceItemInstance> getEtricegen_interfaceiteminstances() {
        return etricegen_interfaceiteminstances;
    }

    public void addEtricegen_interfaceiteminstance(Etricegen_interfaceiteminstance etricegen_interfaceiteminstance) {
        this.etricegen_interfaceiteminstances.add(etricegen_interfaceiteminstance);
    }

}