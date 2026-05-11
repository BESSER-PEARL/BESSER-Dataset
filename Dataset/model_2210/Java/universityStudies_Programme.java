





import java.util.List;
import java.util.ArrayList;

public class universityStudies_Programme  {

    private int numberOfSemesters;
    private String name;
    private String programmeType;





    private universityStudies_Course universitystudies_course;


    public universityStudies_Programme(
        int numberOfSemesters,        String name,        String programmeType    ) {
        this.numberOfSemesters = numberOfSemesters;
        this.name = name;
        this.programmeType = programmeType;
    }


    public int getNumberofsemesters() {
        return numberOfSemesters;
    }

    public void setNumberofsemesters(int numberOfSemesters) {
        this.numberOfSemesters = numberOfSemesters;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getProgrammetype() {
        return programmeType;
    }

    public void setProgrammetype(String programmeType) {
        this.programmeType = programmeType;
    }

    public universityStudies_Course getUniversitystudies_course() {
        return universitystudies_course;
    }

    public void setUniversitystudies_course(universityStudies_Course universitystudies_course) {
        this.universitystudies_course = universitystudies_course;
    }

}