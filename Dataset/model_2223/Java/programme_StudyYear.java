





import java.util.List;
import java.util.ArrayList;

public class programme_StudyYear  {

    private int year;





    private programme_Specialization programme_specialization;




    private programme_Programme programme_programme;


    public programme_StudyYear(
        int year    ) {
        this.year = year;
    }


    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public programme_Specialization getProgramme_specialization() {
        return programme_specialization;
    }

    public void setProgramme_specialization(programme_Specialization programme_specialization) {
        this.programme_specialization = programme_specialization;
    }
    public programme_Programme getProgramme_programme() {
        return programme_programme;
    }

    public void setProgramme_programme(programme_Programme programme_programme) {
        this.programme_programme = programme_programme;
    }

}