





import java.util.List;
import java.util.ArrayList;

public class camel_scalability_NonFunctionalEvent extends SimpleEvent {

    private boolean isViolation;



    public camel_scalability_NonFunctionalEvent(
        boolean isViolation    ) {
        super(
        );
        this.isViolation = isViolation;
    }


    public boolean getIsviolation() {
        return isViolation;
    }

    public void setIsviolation(boolean isViolation) {
        this.isViolation = isViolation;
    }


}