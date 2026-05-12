





import java.util.List;
import java.util.ArrayList;

public class Yahtzee_Display  {

    private String PanelGameName;
    private String PanelPrimary;
    private String PanelNames;
    private String PanelScorecard;
    private String PanelChoices;



    public Yahtzee_Display(
        String PanelGameName,        String PanelPrimary,        String PanelNames,        String PanelScorecard,        String PanelChoices    ) {
        this.PanelGameName = PanelGameName;
        this.PanelPrimary = PanelPrimary;
        this.PanelNames = PanelNames;
        this.PanelScorecard = PanelScorecard;
        this.PanelChoices = PanelChoices;
    }


    public String getPanelgamename() {
        return PanelGameName;
    }

    public void setPanelgamename(String PanelGameName) {
        this.PanelGameName = PanelGameName;
    }
    public String getPanelprimary() {
        return PanelPrimary;
    }

    public void setPanelprimary(String PanelPrimary) {
        this.PanelPrimary = PanelPrimary;
    }
    public String getPanelnames() {
        return PanelNames;
    }

    public void setPanelnames(String PanelNames) {
        this.PanelNames = PanelNames;
    }
    public String getPanelscorecard() {
        return PanelScorecard;
    }

    public void setPanelscorecard(String PanelScorecard) {
        this.PanelScorecard = PanelScorecard;
    }
    public String getPanelchoices() {
        return PanelChoices;
    }

    public void setPanelchoices(String PanelChoices) {
        this.PanelChoices = PanelChoices;
    }


}