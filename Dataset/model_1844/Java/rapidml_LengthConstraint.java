





import java.util.List;
import java.util.ArrayList;

public class rapidml_LengthConstraint extends Constraint {

    private int maxLength;
    private int length;
    private int minLength;



    public rapidml_LengthConstraint(
        int maxLength,        int length,        int minLength    ) {
        super(
        );
        this.maxLength = maxLength;
        this.length = length;
        this.minLength = minLength;
    }


    public int getMaxlength() {
        return maxLength;
    }

    public void setMaxlength(int maxLength) {
        this.maxLength = maxLength;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public int getMinlength() {
        return minLength;
    }

    public void setMinlength(int minLength) {
        this.minLength = minLength;
    }


}