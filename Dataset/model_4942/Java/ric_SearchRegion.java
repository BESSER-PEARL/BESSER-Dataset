





import java.util.List;
import java.util.ArrayList;

public class ric_SearchRegion  {






    private List<ric_Form> ric_forms;




    private ric_Portal ric_portal;


    public ric_SearchRegion(
    ) {
        this.ric_forms = new ArrayList<>();
    }

    public ric_SearchRegion(
        ArrayList<ric_Form> ric_forms    ) {
        this.ric_forms = ric_forms;
    }


    public List<ric_Form> getRic_forms() {
        return ric_forms;
    }

    public void addRic_form(Ric_form ric_form) {
        this.ric_forms.add(ric_form);
    }
    public ric_Portal getRic_portal() {
        return ric_portal;
    }

    public void setRic_portal(ric_Portal ric_portal) {
        this.ric_portal = ric_portal;
    }

}