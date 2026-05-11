





import java.util.List;
import java.util.ArrayList;

public class EFM_RangeOperation extends Operation {

    private int min;
    private int max;





    private EFM_Attribute efm_attribute;


    public EFM_RangeOperation(
        int min,        int max    ) {
        super(
        );
        this.min = min;
        this.max = max;
    }


    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }
    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }

    public EFM_Attribute getEfm_attribute() {
        return efm_attribute;
    }

    public void setEfm_attribute(EFM_Attribute efm_attribute) {
        this.efm_attribute = efm_attribute;
    }

}