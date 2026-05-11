





import java.util.List;
import java.util.ArrayList;

public class model_Player  {

    private String howOut;
    private int runsScored;
    private int noBallsFaced;
    private String noOversBowled;
    private String name;





    private model_Team model_team;




    private model_Innings model_innings;




    private List<model_Over> model_overs;




    private model_Over model_over;




    private model_Innings model_innings;


    public model_Player(
        String howOut,        int runsScored,        int noBallsFaced,        String noOversBowled,        String name    ) {
        this.howOut = howOut;
        this.runsScored = runsScored;
        this.noBallsFaced = noBallsFaced;
        this.noOversBowled = noOversBowled;
        this.name = name;
        this.model_overs = new ArrayList<>();
    }

    public model_Player(
        String howOut,        int runsScored,        int noBallsFaced,        String noOversBowled,        String name        ArrayList<model_Over> model_overs    ) {
        this.howOut = howOut;
        this.runsScored = runsScored;
        this.noBallsFaced = noBallsFaced;
        this.noOversBowled = noOversBowled;
        this.name = name;
        this.model_overs = model_overs;
    }

    public String getHowout() {
        return howOut;
    }

    public void setHowout(String howOut) {
        this.howOut = howOut;
    }
    public int getRunsscored() {
        return runsScored;
    }

    public void setRunsscored(int runsScored) {
        this.runsScored = runsScored;
    }
    public int getNoballsfaced() {
        return noBallsFaced;
    }

    public void setNoballsfaced(int noBallsFaced) {
        this.noBallsFaced = noBallsFaced;
    }
    public String getNooversbowled() {
        return noOversBowled;
    }

    public void setNooversbowled(String noOversBowled) {
        this.noOversBowled = noOversBowled;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_Team getModel_team() {
        return model_team;
    }

    public void setModel_team(model_Team model_team) {
        this.model_team = model_team;
    }
    public model_Innings getModel_innings() {
        return model_innings;
    }

    public void setModel_innings(model_Innings model_innings) {
        this.model_innings = model_innings;
    }
    public List<model_Over> getModel_overs() {
        return model_overs;
    }

    public void addModel_over(Model_over model_over) {
        this.model_overs.add(model_over);
    }
    public model_Over getModel_over() {
        return model_over;
    }

    public void setModel_over(model_Over model_over) {
        this.model_over = model_over;
    }
    public model_Innings getModel_innings() {
        return model_innings;
    }

    public void setModel_innings(model_Innings model_innings) {
        this.model_innings = model_innings;
    }

}