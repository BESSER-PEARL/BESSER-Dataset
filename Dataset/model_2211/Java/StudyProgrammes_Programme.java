





import java.util.List;
import java.util.ArrayList;

public class StudyProgrammes_Programme  {

    private int semestersBeforeSpecialization;
    private String code;
    private String name;
    private int totalNumberOfSemesters;
    private int startYear;





    private StudyProgrammes_Department studyprogrammes_department;


    public StudyProgrammes_Programme(
        int semestersBeforeSpecialization,        String code,        String name,        int totalNumberOfSemesters,        int startYear    ) {
        this.semestersBeforeSpecialization = semestersBeforeSpecialization;
        this.code = code;
        this.name = name;
        this.totalNumberOfSemesters = totalNumberOfSemesters;
        this.startYear = startYear;
    }


    public int getSemestersbeforespecialization() {
        return semestersBeforeSpecialization;
    }

    public void setSemestersbeforespecialization(int semestersBeforeSpecialization) {
        this.semestersBeforeSpecialization = semestersBeforeSpecialization;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getTotalnumberofsemesters() {
        return totalNumberOfSemesters;
    }

    public void setTotalnumberofsemesters(int totalNumberOfSemesters) {
        this.totalNumberOfSemesters = totalNumberOfSemesters;
    }
    public int getStartyear() {
        return startYear;
    }

    public void setStartyear(int startYear) {
        this.startYear = startYear;
    }

    public StudyProgrammes_Department getStudyprogrammes_department() {
        return studyprogrammes_department;
    }

    public void setStudyprogrammes_department(StudyProgrammes_Department studyprogrammes_department) {
        this.studyprogrammes_department = studyprogrammes_department;
    }

}