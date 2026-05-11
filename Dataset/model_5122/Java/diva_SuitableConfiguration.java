





import java.util.List;
import java.util.ArrayList;

public class diva_SuitableConfiguration extends Visitable {

    private int score;





    private diva_ConfigurationModel diva_configurationmodel;


    public diva_SuitableConfiguration(
        int score    ) {
        super(
        );
        this.score = score;
    }


    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }

    public diva_ConfigurationModel getDiva_configurationmodel() {
        return diva_configurationmodel;
    }

    public void setDiva_configurationmodel(diva_ConfigurationModel diva_configurationmodel) {
        this.diva_configurationmodel = diva_configurationmodel;
    }

}