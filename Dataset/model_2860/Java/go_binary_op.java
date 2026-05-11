





import java.util.List;
import java.util.ArrayList;

public class go_binary_op  {

    private String mul_op;
    private String rel_op;
    private String add_op;





    private go_ExpressionLinha go_expressionlinha;


    public go_binary_op(
        String mul_op,        String rel_op,        String add_op    ) {
        this.mul_op = mul_op;
        this.rel_op = rel_op;
        this.add_op = add_op;
    }


    public String getMul_op() {
        return mul_op;
    }

    public void setMul_op(String mul_op) {
        this.mul_op = mul_op;
    }
    public String getRel_op() {
        return rel_op;
    }

    public void setRel_op(String rel_op) {
        this.rel_op = rel_op;
    }
    public String getAdd_op() {
        return add_op;
    }

    public void setAdd_op(String add_op) {
        this.add_op = add_op;
    }

    public go_ExpressionLinha getGo_expressionlinha() {
        return go_expressionlinha;
    }

    public void setGo_expressionlinha(go_ExpressionLinha go_expressionlinha) {
        this.go_expressionlinha = go_expressionlinha;
    }

}