





import java.util.List;
import java.util.ArrayList;

public class archimate_Meaning extends MotivationElement {






    private List<archimate_Stakeholder> archimate_stakeholders;




    private archimate_Stakeholder archimate_stakeholder;


    public archimate_Meaning(
    ) {
        super(
        );
        this.archimate_stakeholders = new ArrayList<>();
    }

    public archimate_Meaning(
        ArrayList<archimate_Stakeholder> archimate_stakeholders    ) {
        this.archimate_stakeholders = archimate_stakeholders;
    }


    public List<archimate_Stakeholder> getArchimate_stakeholders() {
        return archimate_stakeholders;
    }

    public void addArchimate_stakeholder(Archimate_stakeholder archimate_stakeholder) {
        this.archimate_stakeholders.add(archimate_stakeholder);
    }
    public archimate_Stakeholder getArchimate_stakeholder() {
        return archimate_stakeholder;
    }

    public void setArchimate_stakeholder(archimate_Stakeholder archimate_stakeholder) {
        this.archimate_stakeholder = archimate_stakeholder;
    }

}