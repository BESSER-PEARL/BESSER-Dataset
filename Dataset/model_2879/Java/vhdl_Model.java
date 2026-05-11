





import java.util.List;
import java.util.ArrayList;

public class vhdl_Model extends VhdlObject {






    private List<vhdl_DesignUnit> vhdl_designunits;


    public vhdl_Model(
    ) {
        super(
        );
        this.vhdl_designunits = new ArrayList<>();
    }

    public vhdl_Model(
        ArrayList<vhdl_DesignUnit> vhdl_designunits    ) {
        this.vhdl_designunits = vhdl_designunits;
    }


    public List<vhdl_DesignUnit> getVhdl_designunits() {
        return vhdl_designunits;
    }

    public void addVhdl_designunit(Vhdl_designunit vhdl_designunit) {
        this.vhdl_designunits.add(vhdl_designunit);
    }

}