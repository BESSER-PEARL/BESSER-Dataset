





import java.util.List;
import java.util.ArrayList;

public class school_School  {

    private String city;
    private String name;
    private String zipCode;
    private String director;





    private List<school_Classroom> school_classrooms;


    public school_School(
        String city,        String name,        String zipCode,        String director    ) {
        this.city = city;
        this.name = name;
        this.zipCode = zipCode;
        this.director = director;
        this.school_classrooms = new ArrayList<>();
    }

    public school_School(
        String city,        String name,        String zipCode,        String director        ArrayList<school_Classroom> school_classrooms    ) {
        this.city = city;
        this.name = name;
        this.zipCode = zipCode;
        this.director = director;
        this.school_classrooms = school_classrooms;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getZipcode() {
        return zipCode;
    }

    public void setZipcode(String zipCode) {
        this.zipCode = zipCode;
    }
    public String getDirector() {
        return director;
    }

    public void setDirector(String director) {
        this.director = director;
    }

    public List<school_Classroom> getSchool_classrooms() {
        return school_classrooms;
    }

    public void addSchool_classroom(School_classroom school_classroom) {
        this.school_classrooms.add(school_classroom);
    }

}