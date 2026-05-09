





import java.util.List;
import java.util.ArrayList;

public class oclstdlib_Collection extends OclAny {

    private String upper;
    private String lower;



    public oclstdlib_Collection(
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