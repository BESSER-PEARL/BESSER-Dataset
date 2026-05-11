





import java.util.List;
import java.util.ArrayList;

public class units_pc_pc_Pointcut  {






    private List<units_pc_pc_EObject> units_pc_pc_eobjects;


    public units_pc_pc_Pointcut(
    ) {
        this.units_pc_pc_eobjects = new ArrayList<>();
    }

    public units_pc_pc_Pointcut(
        ArrayList<units_pc_pc_EObject> units_pc_pc_eobjects    ) {
        this.units_pc_pc_eobjects = units_pc_pc_eobjects;
    }


    public List<units_pc_pc_EObject> getUnits_pc_pc_eobjects() {
        return units_pc_pc_eobjects;
    }

    public void addUnits_pc_pc_eobject(Units_pc_pc_eobject units_pc_pc_eobject) {
        this.units_pc_pc_eobjects.add(units_pc_pc_eobject);
    }

}