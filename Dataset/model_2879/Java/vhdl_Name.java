





import java.util.List;
import java.util.ArrayList;

public class vhdl_Name extends nature_NatureReference, EntityReference, CallReference, type_TypeReference, MultiName, PackageReference, ComponentReference, configuration_ConfigurationReference {






    private vhdl_DesignUnit vhdl_designunit;




    private vhdl_NameList vhdl_namelist;


    public vhdl_Name(
    ) {
        super(
        );
    }



    public vhdl_DesignUnit getVhdl_designunit() {
        return vhdl_designunit;
    }

    public void setVhdl_designunit(vhdl_DesignUnit vhdl_designunit) {
        this.vhdl_designunit = vhdl_designunit;
    }
    public vhdl_NameList getVhdl_namelist() {
        return vhdl_namelist;
    }

    public void setVhdl_namelist(vhdl_NameList vhdl_namelist) {
        this.vhdl_namelist = vhdl_namelist;
    }

}