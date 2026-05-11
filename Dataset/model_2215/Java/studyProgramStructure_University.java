





import java.util.List;
import java.util.ArrayList;

public class studyProgramStructure_University  {

    private String name;





    private List<studyProgramStructure_Course> studyprogramstructure_courses;




    private List<studyProgramStructure_Program> studyprogramstructure_programs;


    public studyProgramStructure_University(
        String name    ) {
        this.name = name;
        this.studyprogramstructure_courses = new ArrayList<>();
        this.studyprogramstructure_programs = new ArrayList<>();
    }

    public studyProgramStructure_University(
        String name        ArrayList<studyProgramStructure_Course> studyprogramstructure_courses,        ArrayList<studyProgramStructure_Program> studyprogramstructure_programs    ) {
        this.name = name;
        this.studyprogramstructure_courses = studyprogramstructure_courses;
        this.studyprogramstructure_programs = studyprogramstructure_programs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<studyProgramStructure_Course> getStudyprogramstructure_courses() {
        return studyprogramstructure_courses;
    }

    public void addStudyprogramstructure_course(Studyprogramstructure_course studyprogramstructure_course) {
        this.studyprogramstructure_courses.add(studyprogramstructure_course);
    }
    public List<studyProgramStructure_Program> getStudyprogramstructure_programs() {
        return studyprogramstructure_programs;
    }

    public void addStudyprogramstructure_program(Studyprogramstructure_program studyprogramstructure_program) {
        this.studyprogramstructure_programs.add(studyprogramstructure_program);
    }

}