





import java.util.List;
import java.util.ArrayList;

public class art_relaxed_CardinalityElement extends ModelElement {

    private String lower;
    private String upper;



    public art_relaxed_CardinalityElement(
        String lower,        String upper    ) {
        super(
        );
        this.lower = lower;
        this.upper = upper;
    }


    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }
    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }


}