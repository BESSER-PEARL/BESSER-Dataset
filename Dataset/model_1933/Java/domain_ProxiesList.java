





import java.util.List;
import java.util.ArrayList;

public class domain_ProxiesList  {






    private List<domain_TypePointer> domain_typepointers;


    public domain_ProxiesList(
    ) {
        this.domain_typepointers = new ArrayList<>();
    }

    public domain_ProxiesList(
        ArrayList<domain_TypePointer> domain_typepointers    ) {
        this.domain_typepointers = domain_typepointers;
    }


    public List<domain_TypePointer> getDomain_typepointers() {
        return domain_typepointers;
    }

    public void addDomain_typepointer(Domain_typepointer domain_typepointer) {
        this.domain_typepointers.add(domain_typepointer);
    }

}