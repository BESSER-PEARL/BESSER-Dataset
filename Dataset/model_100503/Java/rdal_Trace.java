





import java.util.List;
import java.util.ArrayList;

public class rdal_Trace extends ReferencedDesignElements {






    private List<rdal_Specification> rdal_specifications;


    public rdal_Trace(
    ) {
        super(
        );
        this.rdal_specifications = new ArrayList<>();
    }

    public rdal_Trace(
        ArrayList<rdal_Specification> rdal_specifications    ) {
        this.rdal_specifications = rdal_specifications;
    }


    public List<rdal_Specification> getRdal_specifications() {
        return rdal_specifications;
    }

    public void addRdal_specification(Rdal_specification rdal_specification) {
        this.rdal_specifications.add(rdal_specification);
    }

}