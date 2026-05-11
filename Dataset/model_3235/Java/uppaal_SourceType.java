





import java.util.List;
import java.util.ArrayList;

public class uppaal_SourceType  {

    private String ref;





    private uppaal_DocumentRoot uppaal_documentroot;


    public uppaal_SourceType(
        String ref    ) {
        this.ref = ref;
    }


    public String getRef() {
        return ref;
    }

    public void setRef(String ref) {
        this.ref = ref;
    }

    public uppaal_DocumentRoot getUppaal_documentroot() {
        return uppaal_documentroot;
    }

    public void setUppaal_documentroot(uppaal_DocumentRoot uppaal_documentroot) {
        this.uppaal_documentroot = uppaal_documentroot;
    }

}