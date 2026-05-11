





import java.util.List;
import java.util.ArrayList;

public class HTML_AREA extends BODYElement {

    private String shape;
    private String coords;
    private String ahref;



    public HTML_AREA(
        String shape,        String coords,        String ahref    ) {
        super(
        );
        this.shape = shape;
        this.coords = coords;
        this.ahref = ahref;
    }


    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
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


}