





import java.util.List;
import java.util.ArrayList;

public class courses_University  {

    private String name;





    private List<courses_StudyProgram> courses_studyprograms;


    public courses_University(
        String name    ) {
        this.name = name;
        this.courses_studyprograms = new ArrayList<>();
    }

    public courses_University(
        String name        ArrayList<courses_StudyProgram> courses_studyprograms    ) {
        this.name = name;
        this.courses_studyprograms = courses_studyprograms;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<courses_StudyProgram> getCourses_studyprograms() {
        return courses_studyprograms;
    }

    public void addCourses_studyprogram(Courses_studyprogram courses_studyprogram) {
        this.courses_studyprograms.add(courses_studyprogram);
    }

}