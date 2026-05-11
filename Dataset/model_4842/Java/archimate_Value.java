





import java.util.List;
import java.util.ArrayList;

public class archimate_Value extends MotivationElement {






    private archimate_Stakeholder archimate_stakeholder;




    private List<archimate_Stakeholder> archimate_stakeholders;


    public archimate_Value(
    ) {
        super(
        );
        this.archimate_stakeholders = new ArrayList<>();
    }

    public archimate_Value(
        ArrayList<archimate_Stakeholder> archimate_stakeholders    ) {
        this.archimate_stakeholders = archimate_stakeholders;
    }


    public archimate_Stakeholder getArchimate_stakeholder() {
        return archimate_stakeholder;
    }

    public void setArchimate_stakeholder(archimate_Stakeholder archimate_stakeholder) {
        this.archimate_stakeholder = archimate_stakeholder;
    }
    public List<archimate_Stakeholder> getArchimate_stakeholders() {
        return archimate_stakeholders;
    }

    public void addArchimate_stakeholder(Archimate_stakeholder archimate_stakeholder) {
        this.archimate_stakeholders.add(archimate_stakeholder);
    }

}