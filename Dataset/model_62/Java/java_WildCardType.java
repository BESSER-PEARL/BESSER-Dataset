





import java.util.List;
import java.util.ArrayList;

public class java_WildCardType extends Type {

    private boolean upperBound;



    public java_WildCardType(
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