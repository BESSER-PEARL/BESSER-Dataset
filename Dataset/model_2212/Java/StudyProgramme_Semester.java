





import java.util.List;
import java.util.ArrayList;

public class StudyProgramme_Semester  {

    private String season;
    private String creditConstraint;
    private int number;
    private float totalCredits;





    private StudyProgramme_Programme studyprogramme_programme;


    public StudyProgramme_Semester(
        String season,        String creditConstraint,        int number,        float totalCredits    ) {
        this.season = season;
        this.creditConstraint = creditConstraint;
        this.number = number;
        this.totalCredits = totalCredits;
    }


    public String getSeason() {
        return season;
    }

    public void setSeason(String season) {
        this.season = season;
    }
    public String getCreditconstraint() {
        return creditConstraint;
    }

    public void setCreditconstraint(String creditConstraint) {
        this.creditConstraint = creditConstraint;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public float getTotalcredits() {
        return totalCredits;
    }

    public void setTotalcredits(float totalCredits) {
        this.totalCredits = totalCredits;
    }

    public StudyProgramme_Programme getStudyprogramme_programme() {
        return studyprogramme_programme;
    }

    public void setStudyprogramme_programme(StudyProgramme_Programme studyprogramme_programme) {
        this.studyprogramme_programme = studyprogramme_programme;
    }

}