





import java.util.List;
import java.util.ArrayList;

public class school_School  {

    private String city;
    private String zipCode;
    private String name;
    private String director;





    private school_Diagram school_diagram;




    private List<school_Classroom> school_classrooms;


    public school_School(
        String city,        String zipCode,        String name,        String director    ) {
        this.city = city;
        this.zipCode = zipCode;
        this.name = name;
        this.director = director;
        this.school_classrooms = new ArrayList<>();
    }

    public school_School(
        String city,        String zipCode,        String name,        String director        ArrayList<school_Classroom> school_classrooms    ) {
        this.city = city;
        this.zipCode = zipCode;
        this.name = name;
        this.director = director;
        this.school_classrooms = school_classrooms;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getZipcode() {
        return zipCode;
    }

    public void setZipcode(String zipCode) {
        this.zipCode = zipCode;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDirector() {
        return director;
    }

    public void setDirector(String director) {
        this.director = director;
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