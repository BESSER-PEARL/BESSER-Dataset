





import java.util.List;
import java.util.ArrayList;

public class model_RandomAction extends Action {

    private boolean isRandom;



    public model_RandomAction(
        boolean isRandom    ) {
        super(
        );
        this.isRandom = isRandom;
    }


    public boolean getIsrandom() {
        return isRandom;
    }

    public void setIsrandom(boolean isRandom) {
        this.isRandom = isRandom;
    }


}