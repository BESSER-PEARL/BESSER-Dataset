





import java.util.List;
import java.util.ArrayList;

public class iot2_OpaqueAction extends Action {






    private iot2_OperationDef iot2_operationdef;




    private List<iot2_Expression> iot2_expressions;


    public iot2_OpaqueAction(
    ) {
        super(
        );
        this.iot2_expressions = new ArrayList<>();
    }

    public iot2_OpaqueAction(
        ArrayList<iot2_Expression> iot2_expressions    ) {
        this.iot2_expressions = iot2_expressions;
    }


    public iot2_OperationDef getIot2_operationdef() {
        return iot2_operationdef;
    }

    public void setIot2_operationdef(iot2_OperationDef iot2_operationdef) {
        this.iot2_operationdef = iot2_operationdef;
    }
    public List<iot2_Expression> getIot2_expressions() {
        return iot2_expressions;
    }

    public void addIot2_expression(Iot2_expression iot2_expression) {
        this.iot2_expressions.add(iot2_expression);
    }

}