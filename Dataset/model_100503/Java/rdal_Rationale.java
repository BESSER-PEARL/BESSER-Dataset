





import java.util.List;
import java.util.ArrayList;

public class rdal_Rationale extends IdentifiedElement {






    private List<rdal_Stakeholder> rdal_stakeholders;


    public rdal_Rationale(
    ) {
        super(
        );
        this.rdal_stakeholders = new ArrayList<>();
    }

    public rdal_Rationale(
        ArrayList<rdal_Stakeholder> rdal_stakeholders    ) {
        this.rdal_stakeholders = rdal_stakeholders;
    }


    public List<rdal_Stakeholder> getRdal_stakeholders() {
        return rdal_stakeholders;
    }

    public void addRdal_stakeholder(Rdal_stakeholder rdal_stakeholder) {
        this.rdal_stakeholders.add(rdal_stakeholder);
    }

}