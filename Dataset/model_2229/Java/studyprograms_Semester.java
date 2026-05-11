





import java.util.List;
import java.util.ArrayList;

public class studyprograms_Semester  {

    private String semesterType;
    private String semesterCode;
    private int year;





    private studyprograms_Specialisation studyprograms_specialisation;




    private studyprograms_Programme studyprograms_programme;


    public studyprograms_Semester(
        String semesterType,        String semesterCode,        int year    ) {
        this.semesterType = semesterType;
        this.semesterCode = semesterCode;
        this.year = year;
    }


    public String getSemestertype() {
        return semesterType;
    }

    public void setSemestertype(String semesterType) {
        this.semesterType = semesterType;
    }
    public String getSemestercode() {
        return semesterCode;
    }

    public void setSemestercode(String semesterCode) {
        this.semesterCode = semesterCode;
    }
    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public studyprograms_Specialisation getStudyprograms_specialisation() {
        return studyprograms_specialisation;
    }

    public void setStudyprograms_specialisation(studyprograms_Specialisation studyprograms_specialisation) {
        this.studyprograms_specialisation = studyprograms_specialisation;
    }
    public studyprograms_Programme getStudyprograms_programme() {
        return studyprograms_programme;
    }

    public void setStudyprograms_programme(studyprograms_Programme studyprograms_programme) {
        this.studyprograms_programme = studyprograms_programme;
    }

}