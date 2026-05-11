





import java.util.List;
import java.util.ArrayList;

public class cal_AstTypeParam  {

    private String name;





    private cal_AstType cal_asttype;




    private cal_AstExpression cal_astexpression;


    public cal_AstTypeParam(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cal_AstType getCal_asttype() {
        return cal_asttype;
    }

    public void setCal_asttype(cal_AstType cal_asttype) {
        this.cal_asttype = cal_asttype;
    }
    public cal_AstExpression getCal_astexpression() {
        return cal_astexpression;
    }

    public void setCal_astexpression(cal_AstExpression cal_astexpression) {
        this.cal_astexpression = cal_astexpression;
    }

}