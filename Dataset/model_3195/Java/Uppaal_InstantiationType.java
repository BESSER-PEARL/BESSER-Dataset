





import java.util.List;
import java.util.ArrayList;

public class Uppaal_InstantiationType  {

    private String mixed;





    private Uppaal_DocumentRoot uppaal_documentroot;


    public Uppaal_InstantiationType(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public Uppaal_DocumentRoot getUppaal_documentroot() {
        return uppaal_documentroot;
    }

    public void setUppaal_documentroot(Uppaal_DocumentRoot uppaal_documentroot) {
        this.uppaal_documentroot = uppaal_documentroot;
    }

}