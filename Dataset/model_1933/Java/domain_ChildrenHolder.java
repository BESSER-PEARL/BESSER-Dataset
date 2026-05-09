





import java.util.List;
import java.util.ArrayList;

public class domain_ChildrenHolder  {






    private List<domain_Uielement> domain_uielements;


    public domain_ChildrenHolder(
    ) {
        this.domain_uielements = new ArrayList<>();
    }

    public domain_ChildrenHolder(
        ArrayList<domain_Uielement> domain_uielements    ) {
        this.domain_uielements = domain_uielements;
    }


    public List<domain_Uielement> getDomain_uielements() {
        return domain_uielements;
    }

    public void addDomain_uielement(Domain_uielement domain_uielement) {
        this.domain_uielements.add(domain_uielement);
    }

}