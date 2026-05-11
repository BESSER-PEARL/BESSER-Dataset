





import java.util.List;
import java.util.ArrayList;

public class university_Course  {

    private String id;
    private String name;





    private university_University university_university;


    public university_Course(
        String id,        String name    ) {
        this.id = id;
        this.name = name;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public university_University getUniversity_university() {
        return university_university;
    }

    public void setUniversity_university(university_University university_university) {
        this.university_university = university_university;
    }

}