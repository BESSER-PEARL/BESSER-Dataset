





import java.util.List;
import java.util.ArrayList;

public class StudyProgrammes_Semester  {

    private String code;
    private String semesterSeason;
    private int year;





    private StudyProgrammes_Programme studyprogrammes_programme;




    private StudyProgrammes_Specialization studyprogrammes_specialization;


    public StudyProgrammes_Semester(
        String code,        String semesterSeason,        int year    ) {
        this.code = code;
        this.semesterSeason = semesterSeason;
        this.year = year;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getSemesterseason() {
        return semesterSeason;
    }

    public void setSemesterseason(String semesterSeason) {
        this.semesterSeason = semesterSeason;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public StudyProgrammes_Programme getStudyprogrammes_programme() {
        return studyprogrammes_programme;
    }

    public void setStudyprogrammes_programme(StudyProgrammes_Programme studyprogrammes_programme) {
        this.studyprogrammes_programme = studyprogrammes_programme;
    }
    public StudyProgrammes_Specialization getStudyprogrammes_specialization() {
        return studyprogrammes_specialization;
    }

    public void setStudyprogrammes_specialization(StudyProgrammes_Specialization studyprogrammes_specialization) {
        this.studyprogrammes_specialization = studyprogrammes_specialization;
    }

}