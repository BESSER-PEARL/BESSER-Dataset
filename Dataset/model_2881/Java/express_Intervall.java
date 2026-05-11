





import java.util.List;
import java.util.ArrayList;

public class express_Intervall  {

    private String expression;





    private express_WhereRule express_whererule;


    public express_Intervall(
        String expression    ) {
        this.expression = expression;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public express_WhereRule getExpress_whererule() {
        return express_whererule;
    }

    public void setExpress_whererule(express_WhereRule express_whererule) {
        this.express_whererule = express_whererule;
    }

}