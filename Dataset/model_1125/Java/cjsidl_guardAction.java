





import java.util.List;
import java.util.ArrayList;

public class cjsidl_guardAction  {

    private String not_;
    private String name;





    private List<cjsidl_guardParam> cjsidl_guardparams;




    private cjsidl_guard cjsidl_guard;


    public cjsidl_guardAction(
        String not_,        String name    ) {
        this.not_ = not_;
        this.name = name;
        this.cjsidl_guardparams = new ArrayList<>();
    }

    public cjsidl_guardAction(
        String not_,        String name        ArrayList<cjsidl_guardParam> cjsidl_guardparams    ) {
        this.not_ = not_;
        this.name = name;
        this.cjsidl_guardparams = cjsidl_guardparams;
    }

    public String getNot_() {
        return not_;
    }

    public void setNot_(String not_) {
        this.not_ = not_;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<cjsidl_guardParam> getCjsidl_guardparams() {
        return cjsidl_guardparams;
    }

    public void addCjsidl_guardparam(Cjsidl_guardparam cjsidl_guardparam) {
        this.cjsidl_guardparams.add(cjsidl_guardparam);
    }
    public cjsidl_guard getCjsidl_guard() {
        return cjsidl_guard;
    }

    public void setCjsidl_guard(cjsidl_guard cjsidl_guard) {
        this.cjsidl_guard = cjsidl_guard;
    }

}