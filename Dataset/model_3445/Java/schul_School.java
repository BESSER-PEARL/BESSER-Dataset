





import java.util.List;
import java.util.ArrayList;

public class schul_School  {

    private String name;





    private schul_Diagram schul_diagram;




    private List<schul_Classroom> schul_classrooms;


    public schul_School(
        String name    ) {
        this.name = name;
        this.schul_classrooms = new ArrayList<>();
    }

    public schul_School(
        String name        ArrayList<schul_Classroom> schul_classrooms    ) {
        this.name = name;
        this.schul_classrooms = schul_classrooms;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public schul_Diagram getSchul_diagram() {
        return schul_diagram;
    }

    public void setSchul_diagram(schul_Diagram schul_diagram) {
        this.schul_diagram = schul_diagram;
    }
    public List<schul_Classroom> getSchul_classrooms() {
        return schul_classrooms;
    }

    public void addSchul_classroom(Schul_classroom schul_classroom) {
        this.schul_classrooms.add(schul_classroom);
    }

}