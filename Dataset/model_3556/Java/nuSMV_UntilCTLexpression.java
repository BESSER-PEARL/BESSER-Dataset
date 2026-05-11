





import java.util.List;
import java.util.ArrayList;

public class nuSMV_UntilCTLexpression extends SimpleExpression {

    private String ea;





    private nuSMV_SimpleExpression nusmv_simpleexpression;


    public nuSMV_UntilCTLexpression(
        String ea    ) {
        super(
        );
        this.ea = ea;
    }


    public String getEa() {
        return ea;
    }

    public void setEa(String ea) {
        this.ea = ea;
    }

    public nuSMV_SimpleExpression getNusmv_simpleexpression() {
        return nusmv_simpleexpression;
    }

    public void setNusmv_simpleexpression(nuSMV_SimpleExpression nusmv_simpleexpression) {
        this.nusmv_simpleexpression = nusmv_simpleexpression;
    }

}