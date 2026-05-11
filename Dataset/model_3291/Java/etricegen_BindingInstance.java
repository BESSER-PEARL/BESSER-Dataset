





import java.util.List;
import java.util.ArrayList;

public class etricegen_BindingInstance  {






    private etricegen_StructureInstance etricegen_structureinstance;




    private etricegen_PortInstance etricegen_portinstance;




    private List<etricegen_PortInstance> etricegen_portinstances;


    public etricegen_BindingInstance(
    ) {
        this.etricegen_portinstances = new ArrayList<>();
    }

    public etricegen_BindingInstance(
        ArrayList<etricegen_PortInstance> etricegen_portinstances    ) {
        this.etricegen_portinstances = etricegen_portinstances;
    }


    public etricegen_StructureInstance getEtricegen_structureinstance() {
        return etricegen_structureinstance;
    }

    public void setEtricegen_structureinstance(etricegen_StructureInstance etricegen_structureinstance) {
        this.etricegen_structureinstance = etricegen_structureinstance;
    }
    public etricegen_PortInstance getEtricegen_portinstance() {
        return etricegen_portinstance;
    }

    public void setEtricegen_portinstance(etricegen_PortInstance etricegen_portinstance) {
        this.etricegen_portinstance = etricegen_portinstance;
    }
    public List<etricegen_PortInstance> getEtricegen_portinstances() {
        return etricegen_portinstances;
    }

    public void addEtricegen_portinstance(Etricegen_portinstance etricegen_portinstance) {
        this.etricegen_portinstances.add(etricegen_portinstance);
    }

}