





import java.util.List;
import java.util.ArrayList;

public class school_School  {

    private String name;





    private school_Diagram school_diagram;




    private List<school_Classroom> school_classrooms;


    public school_School(
        String name    ) {
        this.name = name;
        this.school_classrooms = new ArrayList<>();
    }

    public school_School(
        String name        ArrayList<school_Classroom> school_classrooms    ) {
        this.name = name;
        this.school_classrooms = school_classrooms;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public school_Diagram getSchool_diagram() {
        return school_diagram;
    }

    public void setSchool_diagram(school_Diagram school_diagram) {
        this.school_diagram = school_diagram;
    }
    public List<school_Classroom> getSchool_classrooms() {
        return school_classrooms;
    }

    public void addSchool_classroom(School_classroom school_classroom) {
        this.school_classrooms.add(school_classroom);
    }

}