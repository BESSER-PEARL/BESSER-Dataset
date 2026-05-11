





import java.util.List;
import java.util.ArrayList;

public class units_av_av_Advice  {






    private List<units_av_av_EObject> units_av_av_eobjects;


    public units_av_av_Advice(
    ) {
        this.units_av_av_eobjects = new ArrayList<>();
    }

    public units_av_av_Advice(
        ArrayList<units_av_av_EObject> units_av_av_eobjects    ) {
        this.units_av_av_eobjects = units_av_av_eobjects;
    }


    public List<units_av_av_EObject> getUnits_av_av_eobjects() {
        return units_av_av_eobjects;
    }

    public void addUnits_av_av_eobject(Units_av_av_eobject units_av_av_eobject) {
        this.units_av_av_eobjects.add(units_av_av_eobject);
    }

}