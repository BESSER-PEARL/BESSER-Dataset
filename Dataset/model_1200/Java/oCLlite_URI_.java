





import java.util.List;
import java.util.ArrayList;

public class oCLlite_URI_  {

    private String fragment_;
    private String authority;
    private String scheme;





    private oCLlite_OclLModel ocllite_ocllmodel;


    public oCLlite_URI_(
        String fragment_,        String authority,        String scheme    ) {
        this.fragment_ = fragment_;
        this.authority = authority;
        this.scheme = scheme;
    }


    public String getFragment_() {
        return fragment_;
    }

    public void setFragment_(String fragment_) {
        this.fragment_ = fragment_;
    }
    public String getAuthority() {
        return authority;
    }

    public void setAuthority(String authority) {
        this.authority = authority;
    }
    public String getScheme() {
        return scheme;
    }

    public void setScheme(String scheme) {
        this.scheme = scheme;
    }

    public oCLlite_OclLModel getOcllite_ocllmodel() {
        return ocllite_ocllmodel;
    }

    public void setOcllite_ocllmodel(oCLlite_OclLModel ocllite_ocllmodel) {
        this.ocllite_ocllmodel = ocllite_ocllmodel;
    }

}