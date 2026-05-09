





import java.util.List;
import java.util.ArrayList;

public class conf101_System extends NamedElement {






    private List<conf101_Laboratory> conf101_laboratorys;




    private conf101_RevisionProcess conf101_revisionprocess;




    private List<conf101_Conference> conf101_conferences;


    public conf101_System(
    ) {
        super(
        );
        this.conf101_laboratorys = new ArrayList<>();
        this.conf101_conferences = new ArrayList<>();
    }

    public conf101_System(
        ArrayList<conf101_Laboratory> conf101_laboratorys,        ArrayList<conf101_Conference> conf101_conferences    ) {
        this.conf101_laboratorys = conf101_laboratorys;
        this.conf101_conferences = conf101_conferences;
    }


    public List<conf101_Laboratory> getConf101_laboratorys() {
        return conf101_laboratorys;
    }

    public void addConf101_laboratory(Conf101_laboratory conf101_laboratory) {
        this.conf101_laboratorys.add(conf101_laboratory);
    }
    public conf101_RevisionProcess getConf101_revisionprocess() {
        return conf101_revisionprocess;
    }

    public void setConf101_revisionprocess(conf101_RevisionProcess conf101_revisionprocess) {
        this.conf101_revisionprocess = conf101_revisionprocess;
    }
    public List<conf101_Conference> getConf101_conferences() {
        return conf101_conferences;
    }

    public void addConf101_conference(Conf101_conference conf101_conference) {
        this.conf101_conferences.add(conf101_conference);
    }

}