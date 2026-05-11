





import java.util.List;
import java.util.ArrayList;

public class university_Semesters  {

    private int year;
    private String semesterTime;





    private university_University university_university;




    private List<university_ProgrammeSemesters> university_programmesemesterss;




    private university_ProgrammeSemesters university_programmesemesters;




    private university_CourseInstances university_courseinstances;


    public university_Semesters(
        int year,        String semesterTime    ) {
        this.year = year;
        this.semesterTime = semesterTime;
        this.university_programmesemesterss = new ArrayList<>();
    }

    public university_Semesters(
        int year,        String semesterTime        ArrayList<university_ProgrammeSemesters> university_programmesemesterss    ) {
        this.year = year;
        this.semesterTime = semesterTime;
        this.university_programmesemesterss = university_programmesemesterss;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }
    public String getSemestertime() {
        return semesterTime;
    }

    public void setSemestertime(String semesterTime) {
        this.semesterTime = semesterTime;
    }

    public university_University getUniversity_university() {
        return university_university;
    }

    public void setUniversity_university(university_University university_university) {
        this.university_university = university_university;
    }
    public List<university_ProgrammeSemesters> getUniversity_programmesemesterss() {
        return university_programmesemesterss;
    }

    public void addUniversity_programmesemesters(University_programmesemesters university_programmesemesters) {
        this.university_programmesemesterss.add(university_programmesemesters);
    }
    public university_ProgrammeSemesters getUniversity_programmesemesters() {
        return university_programmesemesters;
    }

    public void setUniversity_programmesemesters(university_ProgrammeSemesters university_programmesemesters) {
        this.university_programmesemesters = university_programmesemesters;
    }
    public university_CourseInstances getUniversity_courseinstances() {
        return university_courseinstances;
    }

    public void setUniversity_courseinstances(university_CourseInstances university_courseinstances) {
        this.university_courseinstances = university_courseinstances;
    }

}