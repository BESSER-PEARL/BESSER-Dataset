





import java.util.List;
import java.util.ArrayList;

public class atlext_ATL_Callable  {






    private List<PropertyCallExp> propertycallexps;


    public atlext_ATL_Callable(
    ) {
        this.propertycallexps = new ArrayList<>();
    }

    public atlext_ATL_Callable(
        ArrayList<PropertyCallExp> propertycallexps    ) {
        this.propertycallexps = propertycallexps;
    }


    public List<PropertyCallExp> getPropertycallexps() {
        return propertycallexps;
    }

    public void addPropertycallexp(Propertycallexp propertycallexp) {
        this.propertycallexps.add(propertycallexp);
    }

}