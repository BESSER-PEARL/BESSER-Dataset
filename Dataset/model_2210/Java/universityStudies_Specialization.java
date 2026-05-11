





import java.util.List;
import java.util.ArrayList;

public class universityStudies_Specialization  {

    private String name;





    private universityStudies_Specialization universitystudies_specialization;




    private universityStudies_Programme universitystudies_programme;


    public universityStudies_Specialization(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public universityStudies_Specialization getUniversitystudies_specialization() {
        return universitystudies_specialization;
    }

    public void setUniversitystudies_specialization(universityStudies_Specialization universitystudies_specialization) {
        this.universitystudies_specialization = universitystudies_specialization;
    }
    public universityStudies_Programme getUniversitystudies_programme() {
        return universitystudies_programme;
    }

    public void setUniversitystudies_programme(universityStudies_Programme universitystudies_programme) {
        this.universitystudies_programme = universitystudies_programme;
    }

}