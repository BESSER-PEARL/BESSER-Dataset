





import java.util.List;
import java.util.ArrayList;

public class cobol_operators_LessThan extends RelationalOperator {

    private boolean than;



    public cobol_operators_LessThan(
        boolean than    ) {
        super(
        );
        this.than = than;
    }


    public boolean getThan() {
        return than;
    }

    public void setThan(boolean than) {
        this.than = than;
    }


}