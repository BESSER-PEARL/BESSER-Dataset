





import java.util.List;
import java.util.ArrayList;

public class domain_StyleElement  {






    private List<domain_StyleClass> domain_styleclasss;




    private domain_Context domain_context;


    public domain_StyleElement(
    ) {
        this.domain_styleclasss = new ArrayList<>();
    }

    public domain_StyleElement(
        ArrayList<domain_StyleClass> domain_styleclasss    ) {
        this.domain_styleclasss = domain_styleclasss;
    }


    public List<domain_StyleClass> getDomain_styleclasss() {
        return domain_styleclasss;
    }

    public void addDomain_styleclass(Domain_styleclass domain_styleclass) {
        this.domain_styleclasss.add(domain_styleclass);
    }
    public domain_Context getDomain_context() {
        return domain_context;
    }

    public void setDomain_context(domain_Context domain_context) {
        this.domain_context = domain_context;
    }

}