





import java.util.List;
import java.util.ArrayList;

public class diva_SuitableConfiguration  {

    private int score;





    private List<diva_ConfigVariant> diva_configvariants;




    private diva_ConfigurationModel diva_configurationmodel;


    public diva_SuitableConfiguration(
        int score    ) {
        this.score = score;
        this.diva_configvariants = new ArrayList<>();
    }

    public diva_SuitableConfiguration(
        int score        ArrayList<diva_ConfigVariant> diva_configvariants    ) {
        this.score = score;
        this.diva_configvariants = diva_configvariants;
    }

    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }

    public List<diva_ConfigVariant> getDiva_configvariants() {
        return diva_configvariants;
    }

    public void addDiva_configvariant(Diva_configvariant diva_configvariant) {
        this.diva_configvariants.add(diva_configvariant);
    }
    public diva_ConfigurationModel getDiva_configurationmodel() {
        return diva_configurationmodel;
    }

    public void setDiva_configurationmodel(diva_ConfigurationModel diva_configurationmodel) {
        this.diva_configurationmodel = diva_configurationmodel;
    }

}