





import java.util.List;
import java.util.ArrayList;

public class cal_AstTypeList extends AstType {






    private cal_AstExpression cal_astexpression;




    private cal_AstType cal_asttype;


    public cal_AstTypeList(
    ) {
        super(
        );
    }



    public cal_AstExpression getCal_astexpression() {
        return cal_astexpression;
    }

    public void setCal_astexpression(cal_AstExpression cal_astexpression) {
        this.cal_astexpression = cal_astexpression;
    }
    public cal_AstType getCal_asttype() {
        return cal_asttype;
    }

    public void setCal_asttype(cal_AstType cal_asttype) {
        this.cal_asttype = cal_asttype;
    }

}