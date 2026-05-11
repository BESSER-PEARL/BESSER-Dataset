





import java.util.List;
import java.util.ArrayList;

public class uppaal_NailType  {

    private String y;
    private String x;





    private uppaal_DocumentRoot uppaal_documentroot;


    public uppaal_NailType(
        String y,        String x    ) {
        this.y = y;
        this.x = x;
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

    public uppaal_DocumentRoot getUppaal_documentroot() {
        return uppaal_documentroot;
    }

    public void setUppaal_documentroot(uppaal_DocumentRoot uppaal_documentroot) {
        this.uppaal_documentroot = uppaal_documentroot;
    }

}