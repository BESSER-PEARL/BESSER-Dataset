





import java.util.List;
import java.util.ArrayList;

public class diva_Dimension extends NamedElement {

    private String upper;
    private String lower;



    public diva_Dimension(
        String upper,        String lower    ) {
        super(
        );
        this.upper = upper;
        this.lower = lower;
    }


    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }
    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }


}