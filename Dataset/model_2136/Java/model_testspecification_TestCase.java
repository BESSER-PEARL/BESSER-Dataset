





import java.util.List;
import java.util.ArrayList;

public class model_testspecification_TestCase extends base_IContainer, base_IPositionable {

    private boolean consistent;



    public model_testspecification_TestCase(
        boolean consistent    ) {
        super(
        );
        this.consistent = consistent;
    }


    public boolean getConsistent() {
        return consistent;
    }

    public void setConsistent(boolean consistent) {
        this.consistent = consistent;
    }


}