





import java.util.List;
import java.util.ArrayList;

public class dbl_ReferencePropertyType extends StructuredPropertyType {

    private boolean rawReference;





    private dbl_Pattern dbl_pattern;


    public dbl_ReferencePropertyType(
        boolean rawReference    ) {
        super(
        );
        this.rawReference = rawReference;
    }


    public boolean getRawreference() {
        return rawReference;
    }

    public void setRawreference(boolean rawReference) {
        this.rawReference = rawReference;
    }

    public dbl_Pattern getDbl_pattern() {
        return dbl_pattern;
    }

    public void setDbl_pattern(dbl_Pattern dbl_pattern) {
        this.dbl_pattern = dbl_pattern;
    }

}