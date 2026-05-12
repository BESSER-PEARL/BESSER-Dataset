





import java.util.List;
import java.util.ArrayList;

public class Yahtzee_Display  {

    private String PanelGameName;
    private String PanelScorecard;
    private String PanelChoices;
    private String PanelNames;
    private String PanelPrimary;



    public Yahtzee_Display(
        String PanelGameName,        String PanelScorecard,        String PanelChoices,        String PanelNames,        String PanelPrimary    ) {
        this.PanelGameName = PanelGameName;
        this.PanelScorecard = PanelScorecard;
        this.PanelChoices = PanelChoices;
        this.PanelNames = PanelNames;
        this.PanelPrimary = PanelPrimary;
    }


    public String getPanelgamename() {
        return PanelGameName;
    }

    public void setPanelgamename(String PanelGameName) {
        this.PanelGameName = PanelGameName;
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
    public String getPanelnames() {
        return PanelNames;
    }

    public void setPanelnames(String PanelNames) {
        this.PanelNames = PanelNames;
    }
    public String getPanelprimary() {
        return PanelPrimary;
    }

    public void setPanelprimary(String PanelPrimary) {
        this.PanelPrimary = PanelPrimary;
    }


}