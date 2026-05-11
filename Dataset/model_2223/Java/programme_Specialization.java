





import java.util.List;
import java.util.ArrayList;

public class programme_Specialization  {

    private String name;





    private programme_Programme programme_programme;




    private programme_Specialization programme_specialization;


    public programme_Specialization(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public programme_Programme getProgramme_programme() {
        return programme_programme;
    }

    public void setProgramme_programme(programme_Programme programme_programme) {
        this.programme_programme = programme_programme;
    }
    public programme_Specialization getProgramme_specialization() {
        return programme_specialization;
    }

    public void setProgramme_specialization(programme_Specialization programme_specialization) {
        this.programme_specialization = programme_specialization;
    }

}