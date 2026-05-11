





import java.util.List;
import java.util.ArrayList;

public class Uppaal_NameType  {

    private String y;
    private String x;
    private String mixed;





    private Uppaal_LocationType uppaal_locationtype;




    private Uppaal_DocumentRoot uppaal_documentroot;


    public Uppaal_NameType(
        String y,        String x,        String mixed    ) {
        this.y = y;
        this.x = x;
        this.mixed = mixed;
    }


    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public Uppaal_LocationType getUppaal_locationtype() {
        return uppaal_locationtype;
    }

    public void setUppaal_locationtype(Uppaal_LocationType uppaal_locationtype) {
        this.uppaal_locationtype = uppaal_locationtype;
    }
    public Uppaal_DocumentRoot getUppaal_documentroot() {
        return uppaal_documentroot;
    }

    public void setUppaal_documentroot(Uppaal_DocumentRoot uppaal_documentroot) {
        this.uppaal_documentroot = uppaal_documentroot;
    }

}