





import java.util.List;
import java.util.ArrayList;

public class vhdl_ArchitectureStatement  {

    private String label;





    private vhdl_Architecture vhdl_architecture;


    public vhdl_ArchitectureStatement(
        String label    ) {
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public vhdl_Architecture getVhdl_architecture() {
        return vhdl_architecture;
    }

    public void setVhdl_architecture(vhdl_Architecture vhdl_architecture) {
        this.vhdl_architecture = vhdl_architecture;
    }

}