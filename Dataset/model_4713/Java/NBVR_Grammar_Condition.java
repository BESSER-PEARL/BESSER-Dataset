





import java.util.List;
import java.util.ArrayList;

public class NBVR_Grammar_Condition extends ParseElement {

    private boolean otherwise;



    public NBVR_Grammar_Condition(
        boolean otherwise    ) {
        super(
        );
        this.otherwise = otherwise;
    }


    public boolean getOtherwise() {
        return otherwise;
    }

    public void setOtherwise(boolean otherwise) {
        this.otherwise = otherwise;
    }


}