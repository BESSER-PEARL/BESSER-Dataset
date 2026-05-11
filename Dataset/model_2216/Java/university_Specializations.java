





import java.util.List;
import java.util.ArrayList;

public class university_Specializations  {

    private String name;





    private university_ProgrammeInstances university_programmeinstances;




    private university_ProgrammeInstances university_programmeinstances;




    private List<university_ProgrammeSemesters> university_programmesemesterss;




    private university_ProgrammeSemesters university_programmesemesters;


    public university_Specializations(
        String name    ) {
        this.name = name;
        this.university_programmesemesterss = new ArrayList<>();
    }

    public university_Specializations(
        String name        ArrayList<university_ProgrammeSemesters> university_programmesemesterss    ) {
        this.name = name;
        this.university_programmesemesterss = university_programmesemesterss;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public university_ProgrammeInstances getUniversity_programmeinstances() {
        return university_programmeinstances;
    }

    public void setUniversity_programmeinstances(university_ProgrammeInstances university_programmeinstances) {
        this.university_programmeinstances = university_programmeinstances;
    }
    public university_ProgrammeInstances getUniversity_programmeinstances() {
        return university_programmeinstances;
    }

    public void setUniversity_programmeinstances(university_ProgrammeInstances university_programmeinstances) {
        this.university_programmeinstances = university_programmeinstances;
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

}