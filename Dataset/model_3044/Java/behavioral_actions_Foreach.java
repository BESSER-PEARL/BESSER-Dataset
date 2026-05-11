





import java.util.List;
import java.util.ArrayList;

public class behavioral_actions_Foreach extends SingleBlockStatement {

    private boolean parallel;



    public behavioral_actions_Foreach(
        boolean parallel    ) {
        super(
        );
        this.parallel = parallel;
    }


    public boolean getParallel() {
        return parallel;
    }

    public void setParallel(boolean parallel) {
        this.parallel = parallel;
    }


}