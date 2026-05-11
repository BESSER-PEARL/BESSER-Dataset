





import java.util.List;
import java.util.ArrayList;

public class UML_14_MultiplicityRange  {

    private String upper;
    private String lower;



    public UML_14_MultiplicityRange(
        String upper,        String lower    ) {
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