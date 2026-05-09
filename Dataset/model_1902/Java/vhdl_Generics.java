





import java.util.List;
import java.util.ArrayList;

public class vhdl_Generics  {






    private vhdl_Entity vhdl_entity;




    private List<vhdl_Generic> vhdl_generics;




    private vhdl_Component vhdl_component;


    public vhdl_Generics(
    ) {
        this.vhdl_generics = new ArrayList<>();
    }

    public vhdl_Generics(
        ArrayList<vhdl_Generic> vhdl_generics    ) {
        this.vhdl_generics = vhdl_generics;
    }


    public vhdl_Entity getVhdl_entity() {
        return vhdl_entity;
    }

    public void setVhdl_entity(vhdl_Entity vhdl_entity) {
        this.vhdl_entity = vhdl_entity;
    }
    public List<vhdl_Generic> getVhdl_generics() {
        return vhdl_generics;
    }

    public void addVhdl_generic(Vhdl_generic vhdl_generic) {
        this.vhdl_generics.add(vhdl_generic);
    }
    public vhdl_Component getVhdl_component() {
        return vhdl_component;
    }

    public void setVhdl_component(vhdl_Component vhdl_component) {
        this.vhdl_component = vhdl_component;
    }

}