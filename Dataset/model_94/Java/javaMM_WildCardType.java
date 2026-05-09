





import java.util.List;
import java.util.ArrayList;

public class javaMM_WildCardType extends Type {

    private String upperBound;



    public javaMM_WildCardType(
        String upperBound    ) {
        super(
        );
        this.upperBound = upperBound;
    }


    public String getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(String upperBound) {
        this.upperBound = upperBound;
    }


}