





import java.util.List;
import java.util.ArrayList;

public class notation_CanonicalStyle extends Style {

    private boolean canonical;



    public notation_CanonicalStyle(
        boolean canonical    ) {
        super(
        );
        this.canonical = canonical;
    }


    public boolean getCanonical() {
        return canonical;
    }

    public void setCanonical(boolean canonical) {
        this.canonical = canonical;
    }


}