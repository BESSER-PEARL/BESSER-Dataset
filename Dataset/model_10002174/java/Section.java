





import java.util.List;
import java.util.ArrayList;

public class Section  {

    private String material;





    private Course course;


    public Section(
        String material    ) {
        this.material = material;
    }


    public String getMaterial() {
        return material;
    }

    public void setMaterial(String material) {
        this.material = material;
    }

    public Course getCourse() {
        return course;
    }

    public void setCourse(Course course) {
        this.course = course;
    }

}