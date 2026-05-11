





import java.util.List;
import java.util.ArrayList;

public class Uppaal_NailType  {

    private String x;
    private String y;





    private Uppaal_DocumentRoot uppaal_documentroot;


    public Uppaal_NailType(
        String x,        String y    ) {
        this.x = x;
        this.y = y;
    }


    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }

    public Uppaal_DocumentRoot getUppaal_documentroot() {
        return uppaal_documentroot;
    }

    public void setUppaal_documentroot(Uppaal_DocumentRoot uppaal_documentroot) {
        this.uppaal_documentroot = uppaal_documentroot;
    }

}