





import java.util.List;
import java.util.ArrayList;

public class schol_School  {

    private String name;





    private schol_Diagram schol_diagram;




    private List<schol_Classroom> schol_classrooms;


    public schol_School(
        String name    ) {
        this.name = name;
        this.schol_classrooms = new ArrayList<>();
    }

    public schol_School(
        String name        ArrayList<schol_Classroom> schol_classrooms    ) {
        this.name = name;
        this.schol_classrooms = schol_classrooms;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public schol_Diagram getSchol_diagram() {
        return schol_diagram;
    }

    public void setSchol_diagram(schol_Diagram schol_diagram) {
        this.schol_diagram = schol_diagram;
    }
    public List<schol_Classroom> getSchol_classrooms() {
        return schol_classrooms;
    }

    public void addSchol_classroom(Schol_classroom schol_classroom) {
        this.schol_classrooms.add(schol_classroom);
    }

}