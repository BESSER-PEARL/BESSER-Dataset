





import java.util.List;
import java.util.ArrayList;

public class conf_Researcher extends Person {






    private conf_Laboratory conf_laboratory;




    private conf_RevisionNote conf_revisionnote;




    private conf_Chapter conf_chapter;


    public conf_Researcher(
    ) {
        super(
        );
    }



    public conf_Laboratory getConf_laboratory() {
        return conf_laboratory;
    }

    public void setConf_laboratory(conf_Laboratory conf_laboratory) {
        this.conf_laboratory = conf_laboratory;
    }
    public conf_RevisionNote getConf_revisionnote() {
        return conf_revisionnote;
    }

    public void setConf_revisionnote(conf_RevisionNote conf_revisionnote) {
        this.conf_revisionnote = conf_revisionnote;
    }
    public conf_Chapter getConf_chapter() {
        return conf_chapter;
    }

    public void setConf_chapter(conf_Chapter conf_chapter) {
        this.conf_chapter = conf_chapter;
    }

}