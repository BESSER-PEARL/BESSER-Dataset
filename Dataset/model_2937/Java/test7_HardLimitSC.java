





import java.util.List;
import java.util.ArrayList;

public class test7_HardLimitSC extends SolutionConstraint {

    private String op1;
    private String value2;
    private String op2;
    private String value1;



    public test7_HardLimitSC(
        String op1,        String value2,        String op2,        String value1    ) {
        super(
        );
        this.op1 = op1;
        this.value2 = value2;
        this.op2 = op2;
        this.value1 = value1;
    }


    public String getOp1() {
        return op1;
    }

    public void setOp1(String op1) {
        this.op1 = op1;
    }
    public String getValue2() {
        return value2;
    }

    public void setValue2(String value2) {
        this.value2 = value2;
    }
    public String getOp2() {
        return op2;
    }

    public void setOp2(String op2) {
        this.op2 = op2;
    }
    public String getValue1() {
        return value1;
    }

    public void setValue1(String value1) {
        this.value1 = value1;
    }


}