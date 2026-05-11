





import java.util.List;
import java.util.ArrayList;

public class odemcustom_MappingStatement extends Statement {






    private List<odemcustom_Expression> odemcustom_expressions;


    public odemcustom_MappingStatement(
    ) {
        super(
        );
        this.odemcustom_expressions = new ArrayList<>();
    }

    public odemcustom_MappingStatement(
        ArrayList<odemcustom_Expression> odemcustom_expressions    ) {
        this.odemcustom_expressions = odemcustom_expressions;
    }


    public List<odemcustom_Expression> getOdemcustom_expressions() {
        return odemcustom_expressions;
    }

    public void addOdemcustom_expression(Odemcustom_expression odemcustom_expression) {
        this.odemcustom_expressions.add(odemcustom_expression);
    }

}