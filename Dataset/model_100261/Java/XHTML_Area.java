





import java.util.List;
import java.util.ArrayList;

public class XHTML_Area extends Attrs, EMPTY, Focus, MapElement {

    private String nohref;
    private String shape;



    public XHTML_Area(
        String nohref,        String shape    ) {
        super(
        );
        this.nohref = nohref;
        this.shape = shape;
    }


    public String getNohref() {
        return nohref;
    }

    public void setNohref(String nohref) {
        this.nohref = nohref;
    }
    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }


}