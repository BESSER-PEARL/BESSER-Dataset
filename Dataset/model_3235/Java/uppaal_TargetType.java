





import java.util.List;
import java.util.ArrayList;

public class uppaal_TargetType  {

    private String ref;





    private uppaal_DocumentRoot uppaal_documentroot;


    public uppaal_TargetType(
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