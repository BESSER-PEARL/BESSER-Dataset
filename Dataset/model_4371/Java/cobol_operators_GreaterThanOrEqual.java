





import java.util.List;
import java.util.ArrayList;

public class cobol_operators_GreaterThanOrEqual extends RelationalOperator {

    private boolean than;
    private boolean to;



    public cobol_operators_GreaterThanOrEqual(
        boolean than,        boolean to    ) {
        super(
        );
        this.than = than;
        this.to = to;
    }


    public boolean getThan() {
        return than;
    }

    public void setThan(boolean than) {
        this.than = than;
    }
    public boolean getTo() {
        return to;
    }

    public void setTo(boolean to) {
        this.to = to;
    }


}