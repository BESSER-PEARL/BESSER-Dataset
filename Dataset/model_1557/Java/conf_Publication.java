





import java.util.List;
import java.util.ArrayList;

public class conf_Publication  {






    private conf_Contribution conf_contribution;




    private conf_Laboratory conf_laboratory;


    public conf_Publication(
    ) {
    }



    public conf_Contribution getConf_contribution() {
        return conf_contribution;
    }

    public void setConf_contribution(conf_Contribution conf_contribution) {
        this.conf_contribution = conf_contribution;
    }
    public conf_Laboratory getConf_laboratory() {
        return conf_laboratory;
    }

    public void setConf_laboratory(conf_Laboratory conf_laboratory) {
        this.conf_laboratory = conf_laboratory;
    }

}