





import java.util.List;
import java.util.ArrayList;

public class model_MRange  {

    private int lower;
    private int upper;





    private model_MMultiplicity model_mmultiplicity;


    public model_MRange(
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

    public model_MMultiplicity getModel_mmultiplicity() {
        return model_mmultiplicity;
    }

    public void setModel_mmultiplicity(model_MMultiplicity model_mmultiplicity) {
        this.model_mmultiplicity = model_mmultiplicity;
    }

}