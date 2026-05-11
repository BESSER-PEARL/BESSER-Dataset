





import java.util.List;
import java.util.ArrayList;

public class Uppaal_SystemType  {

    private String mixed;





    private Uppaal_DocumentRoot uppaal_documentroot;




    private Uppaal_NtaType uppaal_ntatype;


    public Uppaal_SystemType(
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
    public Uppaal_NtaType getUppaal_ntatype() {
        return uppaal_ntatype;
    }

    public void setUppaal_ntatype(Uppaal_NtaType uppaal_ntatype) {
        this.uppaal_ntatype = uppaal_ntatype;
    }

}