





import java.util.List;
import java.util.ArrayList;

public class ram_StructuralView  {






    private ram_Aspect ram_aspect;




    private List<ram_Association> ram_associations;




    private List<ram_Type> ram_types;


    public ram_StructuralView(
    ) {
        this.ram_associations = new ArrayList<>();
        this.ram_types = new ArrayList<>();
    }

    public ram_StructuralView(
        ArrayList<ram_Association> ram_associations,        ArrayList<ram_Type> ram_types    ) {
        this.ram_associations = ram_associations;
        this.ram_types = ram_types;
    }


    public ram_Aspect getRam_aspect() {
        return ram_aspect;
    }

    public void setRam_aspect(ram_Aspect ram_aspect) {
        this.ram_aspect = ram_aspect;
    }
    public List<ram_Association> getRam_associations() {
        return ram_associations;
    }

    public void addRam_association(Ram_association ram_association) {
        this.ram_associations.add(ram_association);
    }
    public List<ram_Type> getRam_types() {
        return ram_types;
    }

    public void addRam_type(Ram_type ram_type) {
        this.ram_types.add(ram_type);
    }

}