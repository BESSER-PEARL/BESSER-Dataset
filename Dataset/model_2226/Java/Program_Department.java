





import java.util.List;
import java.util.ArrayList;

public class Program_Department  {

    private String name;





    private List<Program_Course> program_courses;




    private List<Program_Program> program_programs;




    private Program_Course program_course;


    public Program_Department(
        String name    ) {
        this.name = name;
        this.program_courses = new ArrayList<>();
        this.program_programs = new ArrayList<>();
    }

    public Program_Department(
        String name        ArrayList<Program_Course> program_courses,        ArrayList<Program_Program> program_programs    ) {
        this.name = name;
        this.program_courses = program_courses;
        this.program_programs = program_programs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Program_Course> getProgram_courses() {
        return program_courses;
    }

    public void addProgram_course(Program_course program_course) {
        this.program_courses.add(program_course);
    }
    public List<Program_Program> getProgram_programs() {
        return program_programs;
    }

    public void addProgram_program(Program_program program_program) {
        this.program_programs.add(program_program);
    }
    public Program_Course getProgram_course() {
        return program_course;
    }

    public void setProgram_course(Program_Course program_course) {
        this.program_course = program_course;
    }

}