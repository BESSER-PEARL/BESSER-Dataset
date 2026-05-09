





import java.util.List;
import java.util.ArrayList;

public class UML2_Duration extends ValueSpecification {

    private boolean firstTime;



    public UML2_Duration(
        boolean firstTime    ) {
        super(
        );
        this.firstTime = firstTime;
    }


    public boolean getFirsttime() {
        return firstTime;
    }

    public void setFirsttime(boolean firstTime) {
        this.firstTime = firstTime;
    }


}