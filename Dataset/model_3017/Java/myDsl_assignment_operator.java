





import java.util.List;
import java.util.ArrayList;

public class myDsl_assignment_operator  {

    private String xor_assign;
    private String mod_assign;
    private String add_assign;
    private String left_assign;
    private String mul_assign;
    private String sub_assign;
    private String and_assign;
    private String or_assign;
    private String div_assign;
    private String right_assign;





    private myDsl_assignment_expression mydsl_assignment_expression;


    public myDsl_assignment_operator(
        String xor_assign,        String mod_assign,        String add_assign,        String left_assign,        String mul_assign,        String sub_assign,        String and_assign,        String or_assign,        String div_assign,        String right_assign    ) {
        this.xor_assign = xor_assign;
        this.mod_assign = mod_assign;
        this.add_assign = add_assign;
        this.left_assign = left_assign;
        this.mul_assign = mul_assign;
        this.sub_assign = sub_assign;
        this.and_assign = and_assign;
        this.or_assign = or_assign;
        this.div_assign = div_assign;
        this.right_assign = right_assign;
    }


    public String getXor_assign() {
        return xor_assign;
    }

    public void setXor_assign(String xor_assign) {
        this.xor_assign = xor_assign;
    }
    public String getMod_assign() {
        return mod_assign;
    }

    public void setMod_assign(String mod_assign) {
        this.mod_assign = mod_assign;
    }
    public String getAdd_assign() {
        return add_assign;
    }

    public void setAdd_assign(String add_assign) {
        this.add_assign = add_assign;
    }
    public String getLeft_assign() {
        return left_assign;
    }

    public void setLeft_assign(String left_assign) {
        this.left_assign = left_assign;
    }
    public String getMul_assign() {
        return mul_assign;
    }

    public void setMul_assign(String mul_assign) {
        this.mul_assign = mul_assign;
    }
    public String getSub_assign() {
        return sub_assign;
    }

    public void setSub_assign(String sub_assign) {
        this.sub_assign = sub_assign;
    }
    public String getAnd_assign() {
        return and_assign;
    }

    public void setAnd_assign(String and_assign) {
        this.and_assign = and_assign;
    }
    public String getOr_assign() {
        return or_assign;
    }

    public void setOr_assign(String or_assign) {
        this.or_assign = or_assign;
    }
    public String getDiv_assign() {
        return div_assign;
    }

    public void setDiv_assign(String div_assign) {
        this.div_assign = div_assign;
    }
    public String getRight_assign() {
        return right_assign;
    }

    public void setRight_assign(String right_assign) {
        this.right_assign = right_assign;
    }

    public myDsl_assignment_expression getMydsl_assignment_expression() {
        return mydsl_assignment_expression;
    }

    public void setMydsl_assignment_expression(myDsl_assignment_expression mydsl_assignment_expression) {
        this.mydsl_assignment_expression = mydsl_assignment_expression;
    }

}