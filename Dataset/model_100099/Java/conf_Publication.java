





import java.util.List;
import java.util.ArrayList;

public class conf_Publication  {






    private conf_Contribution conf_contribution;




    private conf_Laboratory conf_laboratory;




    private List<conf_Chapter> conf_chapters;


    public conf_Publication(
    ) {
        this.conf_chapters = new ArrayList<>();
    }

    public conf_Publication(
        ArrayList<conf_Chapter> conf_chapters    ) {
        this.conf_chapters = conf_chapters;
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
    public List<conf_Chapter> getConf_chapters() {
        return conf_chapters;
    }

    public void addConf_chapter(Conf_chapter conf_chapter) {
        this.conf_chapters.add(conf_chapter);
    }

}