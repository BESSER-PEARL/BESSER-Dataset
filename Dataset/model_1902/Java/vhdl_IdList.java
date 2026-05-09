





import java.util.List;
import java.util.ArrayList;

public class vhdl_IdList  {






    private List<vhdl_Expression> vhdl_expressions;




    private vhdl_ProcessStatement vhdl_processstatement;


    public vhdl_IdList(
    ) {
        this.vhdl_expressions = new ArrayList<>();
    }

    public vhdl_IdList(
        ArrayList<vhdl_Expression> vhdl_expressions    ) {
        this.vhdl_expressions = vhdl_expressions;
    }


    public List<vhdl_Expression> getVhdl_expressions() {
        return vhdl_expressions;
    }

    public void addVhdl_expression(Vhdl_expression vhdl_expression) {
        this.vhdl_expressions.add(vhdl_expression);
    }
    public vhdl_ProcessStatement getVhdl_processstatement() {
        return vhdl_processstatement;
    }

    public void setVhdl_processstatement(vhdl_ProcessStatement vhdl_processstatement) {
        this.vhdl_processstatement = vhdl_processstatement;
    }

}