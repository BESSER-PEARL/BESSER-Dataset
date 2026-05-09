





import java.util.List;
import java.util.ArrayList;

public class vhdl_PortMapAssociation  {

    private String formal;





    private vhdl_Expression vhdl_expression;




    private vhdl_PortMap vhdl_portmap;


    public vhdl_PortMapAssociation(
        String formal    ) {
        this.formal = formal;
    }


    public String getFormal() {
        return formal;
    }

    public void setFormal(String formal) {
        this.formal = formal;
    }

    public vhdl_Expression getVhdl_expression() {
        return vhdl_expression;
    }

    public void setVhdl_expression(vhdl_Expression vhdl_expression) {
        this.vhdl_expression = vhdl_expression;
    }
    public vhdl_PortMap getVhdl_portmap() {
        return vhdl_portmap;
    }

    public void setVhdl_portmap(vhdl_PortMap vhdl_portmap) {
        this.vhdl_portmap = vhdl_portmap;
    }

}