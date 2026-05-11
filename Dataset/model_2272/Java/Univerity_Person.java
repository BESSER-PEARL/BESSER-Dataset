





import java.util.List;
import java.util.ArrayList;

public class Univerity_Person  {

    private String Email;
    private String Name;





    private Univerity_Courses univerity_courses;




    private Univerity_Person univerity_person;




    private Univerity_Courses univerity_courses;


    public Univerity_Person(
        String Email,        String Name    ) {
        this.Email = Email;
        this.Name = Name;
    }


    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public Univerity_Courses getUniverity_courses() {
        return univerity_courses;
    }

    public void setUniverity_courses(Univerity_Courses univerity_courses) {
        this.univerity_courses = univerity_courses;
    }
    public Univerity_Person getUniverity_person() {
        return univerity_person;
    }

    public void setUniverity_person(Univerity_Person univerity_person) {
        this.univerity_person = univerity_person;
    }
    public Univerity_Courses getUniverity_courses() {
        return univerity_courses;
    }

    public void setUniverity_courses(Univerity_Courses univerity_courses) {
        this.univerity_courses = univerity_courses;
    }

}