





import java.util.List;
import java.util.ArrayList;

public class studyprogramme_Course  {

    private int level;
    private String name;
    private String courseCode;
    private String displayedName;
    private float credits;



    public studyprogramme_Course(
        int level,        String name,        String courseCode,        String displayedName,        float credits    ) {
        this.level = level;
        this.name = name;
        this.courseCode = courseCode;
        this.displayedName = displayedName;
        this.credits = credits;
    }


    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCoursecode() {
        return courseCode;
    }

    public void setCoursecode(String courseCode) {
        this.courseCode = courseCode;
    }
    public String getDisplayedname() {
        return displayedName;
    }

    public void setDisplayedname(String displayedName) {
        this.displayedName = displayedName;
    }
    public float getCredits() {
        return credits;
    }

    public void setCredits(float credits) {
        this.credits = credits;
    }


}