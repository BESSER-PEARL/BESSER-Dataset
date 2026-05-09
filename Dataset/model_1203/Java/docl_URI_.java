





import java.util.List;
import java.util.ArrayList;

public class docl_URI_  {

    private String authority;
    private String fragment_;
    private String scheme;





    private docl_OclModel docl_oclmodel;


    public docl_URI_(
        String authority,        String fragment_,        String scheme    ) {
        this.authority = authority;
        this.fragment_ = fragment_;
        this.scheme = scheme;
    }


    public String getAuthority() {
        return authority;
    }

    public void setAuthority(String authority) {
        this.authority = authority;
    }
    public String getFragment_() {
        return fragment_;
    }

    public void setFragment_(String fragment_) {
        this.fragment_ = fragment_;
    }
    public String getScheme() {
        return scheme;
    }

    public void setScheme(String scheme) {
        this.scheme = scheme;
    }

    public docl_OclModel getDocl_oclmodel() {
        return docl_oclmodel;
    }

    public void setDocl_oclmodel(docl_OclModel docl_oclmodel) {
        this.docl_oclmodel = docl_oclmodel;
    }

}