





import java.util.List;
import java.util.ArrayList;

public class ir_ArgOrVarRef extends Expression {






    private List<ir_Expression> ir_expressions;




    private List<ir_ItemIndex> ir_itemindexs;




    private ir_ArgOrVar ir_argorvar;




    private ir_ConnectivityVariable ir_connectivityvariable;


    public ir_ArgOrVarRef(
    ) {
        super(
        );
        this.ir_expressions = new ArrayList<>();
        this.ir_itemindexs = new ArrayList<>();
    }

    public ir_ArgOrVarRef(
        ArrayList<ir_Expression> ir_expressions,        ArrayList<ir_ItemIndex> ir_itemindexs    ) {
        this.ir_expressions = ir_expressions;
        this.ir_itemindexs = ir_itemindexs;
    }


    public List<ir_Expression> getIr_expressions() {
        return ir_expressions;
    }

    public void addIr_expression(Ir_expression ir_expression) {
        this.ir_expressions.add(ir_expression);
    }
    public List<ir_ItemIndex> getIr_itemindexs() {
        return ir_itemindexs;
    }

    public void addIr_itemindex(Ir_itemindex ir_itemindex) {
        this.ir_itemindexs.add(ir_itemindex);
    }
    public ir_ArgOrVar getIr_argorvar() {
        return ir_argorvar;
    }

    public void setIr_argorvar(ir_ArgOrVar ir_argorvar) {
        this.ir_argorvar = ir_argorvar;
    }
    public ir_ConnectivityVariable getIr_connectivityvariable() {
        return ir_connectivityvariable;
    }

    public void setIr_connectivityvariable(ir_ConnectivityVariable ir_connectivityvariable) {
        this.ir_connectivityvariable = ir_connectivityvariable;
    }

}