





import java.util.List;
import java.util.ArrayList;

public class gast_types_GASTArray extends TypeDecorator {

    private int dimensions;





    private GASTType gasttype;


    public gast_types_GASTArray(
        int dimensions    ) {
        super(
        );
        this.dimensions = dimensions;
    }


    public int getDimensions() {
        return dimensions;
    }

    public void setDimensions(int dimensions) {
        this.dimensions = dimensions;
    }

    public GASTType getGasttype() {
        return gasttype;
    }

    public void setGasttype(GASTType gasttype) {
        this.gasttype = gasttype;
    }

}