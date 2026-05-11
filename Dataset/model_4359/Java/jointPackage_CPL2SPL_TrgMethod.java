





import java.util.List;
import java.util.ArrayList;

public class jointPackage_CPL2SPL_TrgMethod extends TrgSession {

    private String direction;





    private TrgTypeExpression trgtypeexpression;


    public jointPackage_CPL2SPL_TrgMethod(
        String direction    ) {
        super(
        );
        this.direction = direction;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public TrgTypeExpression getTrgtypeexpression() {
        return trgtypeexpression;
    }

    public void setTrgtypeexpression(TrgTypeExpression trgtypeexpression) {
        this.trgtypeexpression = trgtypeexpression;
    }

}