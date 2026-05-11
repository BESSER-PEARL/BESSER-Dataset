





import java.util.List;
import java.util.ArrayList;

public class dbl_ReferencePropertyType extends StructuredPropertyType {

    private boolean rawReference;



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


}