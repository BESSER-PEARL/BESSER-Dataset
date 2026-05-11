





import java.util.List;
import java.util.ArrayList;

public class cal_AstConnectionAttribute  {

    private String name;





    private cal_AstExpression cal_astexpression;




    private cal_AstConnection cal_astconnection;


    public cal_AstConnectionAttribute(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cal_AstExpression getCal_astexpression() {
        return cal_astexpression;
    }

    public void setCal_astexpression(cal_AstExpression cal_astexpression) {
        this.cal_astexpression = cal_astexpression;
    }
    public cal_AstConnection getCal_astconnection() {
        return cal_astconnection;
    }

    public void setCal_astconnection(cal_AstConnection cal_astconnection) {
        this.cal_astconnection = cal_astconnection;
    }

}