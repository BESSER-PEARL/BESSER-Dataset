





import java.util.List;
import java.util.ArrayList;

public class flat11_LocationType  {

    private String id;
    private String y;
    private String color;
    private String x;





    private flat11_CommittedType flat11_committedtype;




    private flat11_DocumentRoot flat11_documentroot;


    public flat11_LocationType(
        String id,        String y,        String color,        String x    ) {
        this.id = id;
        this.y = y;
        this.color = color;
        this.x = x;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }

    public flat11_CommittedType getFlat11_committedtype() {
        return flat11_committedtype;
    }

    public void setFlat11_committedtype(flat11_CommittedType flat11_committedtype) {
        this.flat11_committedtype = flat11_committedtype;
    }
    public flat11_DocumentRoot getFlat11_documentroot() {
        return flat11_documentroot;
    }

    public void setFlat11_documentroot(flat11_DocumentRoot flat11_documentroot) {
        this.flat11_documentroot = flat11_documentroot;
    }

}