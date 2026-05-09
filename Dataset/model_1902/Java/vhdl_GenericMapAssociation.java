





import java.util.List;
import java.util.ArrayList;

public class vhdl_GenericMapAssociation  {

    private String formal;





    private vhdl_GenericMap vhdl_genericmap;




    private vhdl_Expression vhdl_expression;


    public vhdl_GenericMapAssociation(
        String formal    ) {
        this.formal = formal;
    }


    public String getFormal() {
        return formal;
    }

    public void setFormal(String formal) {
        this.formal = formal;
    }

    public vhdl_GenericMap getVhdl_genericmap() {
        return vhdl_genericmap;
    }

    public void setVhdl_genericmap(vhdl_GenericMap vhdl_genericmap) {
        this.vhdl_genericmap = vhdl_genericmap;
    }
    public vhdl_Expression getVhdl_expression() {
        return vhdl_expression;
    }

    public void setVhdl_expression(vhdl_Expression vhdl_expression) {
        this.vhdl_expression = vhdl_expression;
    }

}