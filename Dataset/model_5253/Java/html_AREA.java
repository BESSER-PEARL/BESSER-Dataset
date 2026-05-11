





import java.util.List;
import java.util.ArrayList;

public class html_AREA extends BODYElement {

    private String shape;
    private String ahref;
    private String coords;



    public html_AREA(
        String shape,        String ahref,        String coords    ) {
        super(
        );
        this.shape = shape;
        this.ahref = ahref;
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
    public String getCoords() {
        return coords;
    }

    public void setCoords(String coords) {
        this.coords = coords;
    }


}