





import java.util.List;
import java.util.ArrayList;

public class conf101_Publication extends NamedElement {






    private List<conf101_Chapter> conf101_chapters;




    private conf101_Contribution conf101_contribution;




    private conf101_Laboratory conf101_laboratory;


    public conf101_Publication(
    ) {
        super(
        );
        this.conf101_chapters = new ArrayList<>();
    }

    public conf101_Publication(
        ArrayList<conf101_Chapter> conf101_chapters    ) {
        this.conf101_chapters = conf101_chapters;
    }


    public List<conf101_Chapter> getConf101_chapters() {
        return conf101_chapters;
    }

    public void addConf101_chapter(Conf101_chapter conf101_chapter) {
        this.conf101_chapters.add(conf101_chapter);
    }
    public conf101_Contribution getConf101_contribution() {
        return conf101_contribution;
    }

    public void setConf101_contribution(conf101_Contribution conf101_contribution) {
        this.conf101_contribution = conf101_contribution;
    }
    public conf101_Laboratory getConf101_laboratory() {
        return conf101_laboratory;
    }

    public void setConf101_laboratory(conf101_Laboratory conf101_laboratory) {
        this.conf101_laboratory = conf101_laboratory;
    }

}