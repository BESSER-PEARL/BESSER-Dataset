





import java.util.List;
import java.util.ArrayList;

public class vhdl_LibraryUnit  {

    private String name;





    private vhdl_DesignFile vhdl_designfile;


    public vhdl_LibraryUnit(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public vhdl_DesignFile getVhdl_designfile() {
        return vhdl_designfile;
    }

    public void setVhdl_designfile(vhdl_DesignFile vhdl_designfile) {
        this.vhdl_designfile = vhdl_designfile;
    }

}