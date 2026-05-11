





import java.util.List;
import java.util.ArrayList;

public class Uppaal_SourceType  {

    private String ref;





    private Uppaal_DocumentRoot uppaal_documentroot;


    public Uppaal_SourceType(
        String ref    ) {
        this.ref = ref;
    }


    public String getRef() {
        return ref;
    }

    public void setRef(String ref) {
        this.ref = ref;
    }

    public Uppaal_DocumentRoot getUppaal_documentroot() {
        return uppaal_documentroot;
    }

    public void setUppaal_documentroot(Uppaal_DocumentRoot uppaal_documentroot) {
        this.uppaal_documentroot = uppaal_documentroot;
    }

}