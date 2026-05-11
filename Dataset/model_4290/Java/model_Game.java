




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_Game  {

    private String venue;
    private LocalDate date;





    private List<model_Innings> model_inningss;




    private List<model_Team> model_teams;


    public model_Game(
        String venue,        LocalDate date    ) {
        this.venue = venue;
        this.date = date;
        this.model_inningss = new ArrayList<>();
        this.model_teams = new ArrayList<>();
    }

    public model_Game(
        String venue,        LocalDate date        ArrayList<model_Innings> model_inningss,        ArrayList<model_Team> model_teams    ) {
        this.venue = venue;
        this.date = date;
        this.model_inningss = model_inningss;
        this.model_teams = model_teams;
    }

    public String getVenue() {
        return venue;
    }

    public void setVenue(String venue) {
        this.venue = venue;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public List<model_Innings> getModel_inningss() {
        return model_inningss;
    }

    public void addModel_innings(Model_innings model_innings) {
        this.model_inningss.add(model_innings);
    }
    public List<model_Team> getModel_teams() {
        return model_teams;
    }

    public void addModel_team(Model_team model_team) {
        this.model_teams.add(model_team);
    }

}