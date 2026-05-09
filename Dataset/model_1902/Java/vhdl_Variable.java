





import java.util.List;
import java.util.ArrayList;

public class vhdl_Variable extends Expression {

    private String name;





    private vhdl_Variable vhdl_variable;


    public vhdl_Variable(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public vhdl_Variable getVhdl_variable() {
        return vhdl_variable;
    }

    public void setVhdl_variable(vhdl_Variable vhdl_variable) {
        this.vhdl_variable = vhdl_variable;
    }

}