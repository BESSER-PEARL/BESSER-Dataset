





import java.util.List;
import java.util.ArrayList;

public class roverDSL_BBLiteral extends ValueExpression {

    private boolean bValue;



    public roverDSL_BBLiteral(
        boolean bValue    ) {
        super(
        );
        this.bValue = bValue;
    }


    public boolean getBvalue() {
        return bValue;
    }

    public void setBvalue(boolean bValue) {
        this.bValue = bValue;
    }


}