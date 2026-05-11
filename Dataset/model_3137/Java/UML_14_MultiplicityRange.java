





import java.util.List;
import java.util.ArrayList;

public class UML_14_MultiplicityRange  {

    private int lower;
    private int upper;



    public UML_14_MultiplicityRange(
        int lower,        int upper    ) {
        this.lower = lower;
        this.upper = upper;
    }


    public int getLower() {
        return lower;
    }

    public void setLower(int lower) {
        this.lower = lower;
    }
    public int getUpper() {
        return upper;
    }

    public void setUpper(int upper) {
        this.upper = upper;
    }


}