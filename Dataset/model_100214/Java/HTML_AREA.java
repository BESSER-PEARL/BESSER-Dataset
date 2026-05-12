





import java.util.List;
import java.util.ArrayList;

public class HTML_AREA extends BODYElement {

    private String coords;
    private String ahref;
    private String shape;



    public HTML_AREA(
        String coords,        String ahref,        String shape    ) {
        super(
        );
        this.coords = coords;
        this.ahref = ahref;
        this.shape = shape;
    }


    public String getCoords() {
        return coords;
    }

    public void setCoords(String coords) {
        this.coords = coords;
    }
    public String getAhref() {
        return ahref;
    }

    public void setAhref(String ahref) {
        this.ahref = ahref;
    }
    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }


}