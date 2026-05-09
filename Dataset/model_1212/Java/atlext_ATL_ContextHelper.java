





import java.util.List;
import java.util.ArrayList;

public class atlext_ATL_ContextHelper  {






    private List<PropertyCallExp> propertycallexps;




    private ATL_atlext_Type atl_atlext_type;


    public atlext_ATL_ContextHelper(
    ) {
        this.propertycallexps = new ArrayList<>();
    }

    public atlext_ATL_ContextHelper(
        ArrayList<PropertyCallExp> propertycallexps    ) {
        this.propertycallexps = propertycallexps;
    }


    public List<PropertyCallExp> getPropertycallexps() {
        return propertycallexps;
    }

    public void addPropertycallexp(Propertycallexp propertycallexp) {
        this.propertycallexps.add(propertycallexp);
    }
    public ATL_atlext_Type getAtl_atlext_type() {
        return atl_atlext_type;
    }

    public void setAtl_atlext_type(ATL_atlext_Type atl_atlext_type) {
        this.atl_atlext_type = atl_atlext_type;
    }

}