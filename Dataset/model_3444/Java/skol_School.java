





import java.util.List;
import java.util.ArrayList;

public class skol_School  {

    private String name;





    private List<skol_Classroom> skol_classrooms;




    private skol_Diagram skol_diagram;


    public skol_School(
        String name    ) {
        this.name = name;
        this.skol_classrooms = new ArrayList<>();
    }

    public skol_School(
        String name        ArrayList<skol_Classroom> skol_classrooms    ) {
        this.name = name;
        this.skol_classrooms = skol_classrooms;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<skol_Classroom> getSkol_classrooms() {
        return skol_classrooms;
    }

    public void addSkol_classroom(Skol_classroom skol_classroom) {
        this.skol_classrooms.add(skol_classroom);
    }
    public skol_Diagram getSkol_diagram() {
        return skol_diagram;
    }

    public void setSkol_diagram(skol_Diagram skol_diagram) {
        this.skol_diagram = skol_diagram;
    }

}