





import java.util.List;
import java.util.ArrayList;

public class gpfl_PortLit extends GExpression {

    private boolean inSide;



    public gpfl_PortLit(
        boolean inSide    ) {
        super(
        );
        this.inSide = inSide;
    }


    public boolean getInside() {
        return inSide;
    }

    public void setInside(boolean inSide) {
        this.inSide = inSide;
    }


}