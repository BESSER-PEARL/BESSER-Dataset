





import java.util.List;
import java.util.ArrayList;

public class hydraconstraints_Number extends NumOperandChoices {

    private int numValue;



    public hydraconstraints_Number(
        int numValue    ) {
        super(
        );
        this.numValue = numValue;
    }


    public int getNumvalue() {
        return numValue;
    }

    public void setNumvalue(int numValue) {
        this.numValue = numValue;
    }


}