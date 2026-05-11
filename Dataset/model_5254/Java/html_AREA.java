





import java.util.List;
import java.util.ArrayList;

public class html_AREA extends BODYElement {

    private String ahref;
    private String shape;
    private String coords;



    public html_AREA(
        String ahref,        String shape,        String coords    ) {
        super(
        );
        this.ahref = ahref;
        this.shape = shape;
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
    public String getCoords() {
        return coords;
    }

    public void setCoords(String coords) {
        this.coords = coords;
    }


}