





import java.util.List;
import java.util.ArrayList;

public class vhdl_Member extends Expression {






    private List<vhdl_Expression> vhdl_expressions;


    public vhdl_Member(
    ) {
        super(
        );
        this.vhdl_expressions = new ArrayList<>();
    }

    public vhdl_Member(
        ArrayList<vhdl_Expression> vhdl_expressions    ) {
        this.vhdl_expressions = vhdl_expressions;
    }


    public List<vhdl_Expression> getVhdl_expressions() {
        return vhdl_expressions;
    }

    public void addVhdl_expression(Vhdl_expression vhdl_expression) {
        this.vhdl_expressions.add(vhdl_expression);
    }

}