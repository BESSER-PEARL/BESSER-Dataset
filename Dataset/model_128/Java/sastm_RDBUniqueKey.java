





import java.util.List;
import java.util.ArrayList;

public class sastm_RDBUniqueKey extends RDBConstraint {






    private List<IncludeUnit> includeunits;


    public sastm_RDBUniqueKey(
    ) {
        super(
        );
        this.includeunits = new ArrayList<>();
    }

    public sastm_RDBUniqueKey(
        ArrayList<IncludeUnit> includeunits    ) {
        this.includeunits = includeunits;
    }


    public List<IncludeUnit> getIncludeunits() {
        return includeunits;
    }

    public void addIncludeunit(Includeunit includeunit) {
        this.includeunits.add(includeunit);
    }

}