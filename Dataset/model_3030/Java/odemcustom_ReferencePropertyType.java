





import java.util.List;
import java.util.ArrayList;

public class odemcustom_ReferencePropertyType extends StructuredPropertyType {

    private boolean rawReference;





    private odemcustom_Pattern odemcustom_pattern;


    public odemcustom_ReferencePropertyType(
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

    public odemcustom_Pattern getOdemcustom_pattern() {
        return odemcustom_pattern;
    }

    public void setOdemcustom_pattern(odemcustom_Pattern odemcustom_pattern) {
        this.odemcustom_pattern = odemcustom_pattern;
    }

}