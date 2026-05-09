





import java.util.List;
import java.util.ArrayList;

public class javaMM_WildCardType extends Type {

    private boolean upperBound;



    public javaMM_WildCardType(
        boolean upperBound    ) {
        super(
        );
        this.upperBound = upperBound;
    }


    public boolean getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(boolean upperBound) {
        this.upperBound = upperBound;
    }


}