





import java.util.List;
import java.util.ArrayList;

public class courses_Coursework  {

    private int numSpecHour;
    private int numLabHour;
    private String location;
    private int numLectHour;
    private String instructionLanguage;
    private int termNumber;
    private String teachingSemester;





    private courses_CourseInstance courses_courseinstance;


    public courses_Coursework(
        int numSpecHour,        int numLabHour,        String location,        int numLectHour,        String instructionLanguage,        int termNumber,        String teachingSemester    ) {
        this.numSpecHour = numSpecHour;
        this.numLabHour = numLabHour;
        this.location = location;
        this.numLectHour = numLectHour;
        this.instructionLanguage = instructionLanguage;
        this.termNumber = termNumber;
        this.teachingSemester = teachingSemester;
    }


    public int getNumspechour() {
        return numSpecHour;
    }

    public void setNumspechour(int numSpecHour) {
        this.numSpecHour = numSpecHour;
    }
    public int getNumlabhour() {
        return numLabHour;
    }

    public void setNumlabhour(int numLabHour) {
        this.numLabHour = numLabHour;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public int getNumlecthour() {
        return numLectHour;
    }

    public void setNumlecthour(int numLectHour) {
        this.numLectHour = numLectHour;
    }
    public String getInstructionlanguage() {
        return instructionLanguage;
    }

    public void setInstructionlanguage(String instructionLanguage) {
        this.instructionLanguage = instructionLanguage;
    }
    public int getTermnumber() {
        return termNumber;
    }

    public void setTermnumber(int termNumber) {
        this.termNumber = termNumber;
    }
    public String getTeachingsemester() {
        return teachingSemester;
    }

    public void setTeachingsemester(String teachingSemester) {
        this.teachingSemester = teachingSemester;
    }

    public courses_CourseInstance getCourses_courseinstance() {
        return courses_courseinstance;
    }

    public void setCourses_courseinstance(courses_CourseInstance courses_courseinstance) {
        this.courses_courseinstance = courses_courseinstance;
    }

}