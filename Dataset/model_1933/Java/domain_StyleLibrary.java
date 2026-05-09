





import java.util.List;
import java.util.ArrayList;

public class domain_StyleLibrary  {

    private String name;
    private String uid;





    private List<domain_StyleSet> domain_stylesets;




    private domain_Styles domain_styles;


    public domain_StyleLibrary(
        String name,        String uid    ) {
        this.name = name;
        this.uid = uid;
        this.domain_stylesets = new ArrayList<>();
    }

    public domain_StyleLibrary(
        String name,        String uid        ArrayList<domain_StyleSet> domain_stylesets    ) {
        this.name = name;
        this.uid = uid;
        this.domain_stylesets = domain_stylesets;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }

    public List<domain_StyleSet> getDomain_stylesets() {
        return domain_stylesets;
    }

    public void addDomain_styleset(Domain_styleset domain_styleset) {
        this.domain_stylesets.add(domain_styleset);
    }
    public domain_Styles getDomain_styles() {
        return domain_styles;
    }

    public void setDomain_styles(domain_Styles domain_styles) {
        this.domain_styles = domain_styles;
    }

}