





import java.util.List;
import java.util.ArrayList;

public class morel_PathConstraint extends LinkConstraint {

    private int minLength;
    private int maxLength;



    public morel_PathConstraint(
        int minLength,        int maxLength    ) {
        super(
        );
        this.minLength = minLength;
        this.maxLength = maxLength;
    }


    public int getMinlength() {
        return minLength;
    }

    public void setMinlength(int minLength) {
        this.minLength = minLength;
    }
    public int getMaxlength() {
        return maxLength;
    }

    public void setMaxlength(int maxLength) {
        this.maxLength = maxLength;
    }


}