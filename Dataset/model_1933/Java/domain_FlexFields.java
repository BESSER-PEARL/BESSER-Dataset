





import java.util.List;
import java.util.ArrayList;

public class domain_FlexFields  {






    private List<domain_FlexField> domain_flexfields;


    public domain_FlexFields(
    ) {
        this.domain_flexfields = new ArrayList<>();
    }

    public domain_FlexFields(
        ArrayList<domain_FlexField> domain_flexfields    ) {
        this.domain_flexfields = domain_flexfields;
    }


    public List<domain_FlexField> getDomain_flexfields() {
        return domain_flexfields;
    }

    public void addDomain_flexfield(Domain_flexfield domain_flexfield) {
        this.domain_flexfields.add(domain_flexfield);
    }

}