





import java.util.List;
import java.util.ArrayList;

public class HTML_AREA extends BODYElement {

    private String coords;
    private String shape;
    private String ahref;



    public HTML_AREA(
        String coords,        String shape,        String ahref    ) {
        super(
        );
        this.coords = coords;
        this.shape = shape;
        this.ahref = ahref;
    }


    public String getCoords() {
        return coords;
    }

    public void setCoords(String coords) {
        this.coords = coords;
    }
    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }
    public String getAhref() {
        return ahref;
    }

    public void setAhref(String ahref) {
        this.ahref = ahref;
    }


}