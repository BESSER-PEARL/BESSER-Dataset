





import java.util.List;
import java.util.ArrayList;

public class study_Department  {

    private String name;





    private study_Programme study_programme;




    private List<study_Programme> study_programmes;


    public study_Department(
        String name    ) {
        this.name = name;
        this.study_programmes = new ArrayList<>();
    }

    public study_Department(
        String name        ArrayList<study_Programme> study_programmes    ) {
        this.name = name;
        this.study_programmes = study_programmes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public study_Programme getStudy_programme() {
        return study_programme;
    }

    public void setStudy_programme(study_Programme study_programme) {
        this.study_programme = study_programme;
    }
    public List<study_Programme> getStudy_programmes() {
        return study_programmes;
    }

    public void addStudy_programme(Study_programme study_programme) {
        this.study_programmes.add(study_programme);
    }

}