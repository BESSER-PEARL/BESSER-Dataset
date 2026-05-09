





import java.util.List;
import java.util.ArrayList;

public class conf101_Researcher extends Person {






    private conf101_Chapter conf101_chapter;




    private conf101_Laboratory conf101_laboratory;




    private List<conf101_Publication> conf101_publications;




    private conf101_Evaluation conf101_evaluation;


    public conf101_Researcher(
    ) {
        super(
        );
        this.conf101_publications = new ArrayList<>();
    }

    public conf101_Researcher(
        ArrayList<conf101_Publication> conf101_publications    ) {
        this.conf101_publications = conf101_publications;
    }


    public conf101_Chapter getConf101_chapter() {
        return conf101_chapter;
    }

    public void setConf101_chapter(conf101_Chapter conf101_chapter) {
        this.conf101_chapter = conf101_chapter;
    }
    public conf101_Laboratory getConf101_laboratory() {
        return conf101_laboratory;
    }

    public void setConf101_laboratory(conf101_Laboratory conf101_laboratory) {
        this.conf101_laboratory = conf101_laboratory;
    }
    public List<conf101_Publication> getConf101_publications() {
        return conf101_publications;
    }

    public void addConf101_publication(Conf101_publication conf101_publication) {
        this.conf101_publications.add(conf101_publication);
    }
    public conf101_Evaluation getConf101_evaluation() {
        return conf101_evaluation;
    }

    public void setConf101_evaluation(conf101_Evaluation conf101_evaluation) {
        this.conf101_evaluation = conf101_evaluation;
    }

}