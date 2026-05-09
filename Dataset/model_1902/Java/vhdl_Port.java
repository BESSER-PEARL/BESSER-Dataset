





import java.util.List;
import java.util.ArrayList;

public class vhdl_Port extends Variable {

    private String kind;
    private String mode;





    private vhdl_Ports vhdl_ports;




    private vhdl_Expression vhdl_expression;


    public vhdl_Port(
        String kind,        String mode    ) {
        super(
        );
        this.kind = kind;
        this.mode = mode;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    public vhdl_Ports getVhdl_ports() {
        return vhdl_ports;
    }

    public void setVhdl_ports(vhdl_Ports vhdl_ports) {
        this.vhdl_ports = vhdl_ports;
    }
    public vhdl_Expression getVhdl_expression() {
        return vhdl_expression;
    }

    public void setVhdl_expression(vhdl_Expression vhdl_expression) {
        this.vhdl_expression = vhdl_expression;
    }

}