





import java.util.List;
import java.util.ArrayList;

public class pivot_CallExp extends OCLExpression {

    private String isImplicit;
    private String isSafe;





    private pivot_OCLExpression pivot_oclexpression;


    public pivot_CallExp(
        String isImplicit,        String isSafe    ) {
        super(
        );
        this.isImplicit = isImplicit;
        this.isSafe = isSafe;
    }


    public String getIsimplicit() {
        return isImplicit;
    }

    public void setIsimplicit(String isImplicit) {
        this.isImplicit = isImplicit;
    }
    public String getIssafe() {
        return isSafe;
    }

    public void setIssafe(String isSafe) {
        this.isSafe = isSafe;
    }

    public pivot_OCLExpression getPivot_oclexpression() {
        return pivot_oclexpression;
    }

    public void setPivot_oclexpression(pivot_OCLExpression pivot_oclexpression) {
        this.pivot_oclexpression = pivot_oclexpression;
    }

}