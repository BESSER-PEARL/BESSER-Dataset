





import java.util.List;
import java.util.ArrayList;

public class jPQL_LeftJoin extends FromJoin {

    private boolean isOuter;



    public jPQL_LeftJoin(
        boolean isOuter    ) {
        super(
        );
        this.isOuter = isOuter;
    }


    public boolean getIsouter() {
        return isOuter;
    }

    public void setIsouter(boolean isOuter) {
        this.isOuter = isOuter;
    }


}