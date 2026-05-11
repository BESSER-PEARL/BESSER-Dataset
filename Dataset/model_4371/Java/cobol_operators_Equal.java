





import java.util.List;
import java.util.ArrayList;

public class cobol_operators_Equal extends RelationalOperator {

    private boolean to;



    public cobol_operators_Equal(
        boolean to    ) {
        super(
        );
        this.to = to;
    }


    public boolean getTo() {
        return to;
    }

    public void setTo(boolean to) {
        this.to = to;
    }


}