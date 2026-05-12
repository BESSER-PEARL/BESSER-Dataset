





import java.util.List;
import java.util.ArrayList;

public class metaCompo_mComp  {

    private String type;
    private String name;





    private metaCompo_mFSM metacompo_mfsm;




    private List<metaCompo_mFSM> metacompo_mfsms;




    private metaCompo_mComp metacompo_mcomp;




    private List<metaCompo_mPort> metacompo_mports;




    private List<metaCompo_mVariable> metacompo_mvariables;


    public metaCompo_mComp(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
        this.metacompo_mfsms = new ArrayList<>();
        this.metacompo_mports = new ArrayList<>();
        this.metacompo_mvariables = new ArrayList<>();
    }

    public metaCompo_mComp(
        String type,        String name        ArrayList<metaCompo_mFSM> metacompo_mfsms,        ArrayList<metaCompo_mPort> metacompo_mports,        ArrayList<metaCompo_mVariable> metacompo_mvariables    ) {
        this.type = type;
        this.name = name;
        this.metacompo_mfsms = metacompo_mfsms;
        this.metacompo_mports = metacompo_mports;
        this.metacompo_mvariables = metacompo_mvariables;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public metaCompo_mFSM getMetacompo_mfsm() {
        return metacompo_mfsm;
    }

    public void setMetacompo_mfsm(metaCompo_mFSM metacompo_mfsm) {
        this.metacompo_mfsm = metacompo_mfsm;
    }
    public List<metaCompo_mFSM> getMetacompo_mfsms() {
        return metacompo_mfsms;
    }

    public void addMetacompo_mfsm(Metacompo_mfsm metacompo_mfsm) {
        this.metacompo_mfsms.add(metacompo_mfsm);
    }
    public metaCompo_mComp getMetacompo_mcomp() {
        return metacompo_mcomp;
    }

    public void setMetacompo_mcomp(metaCompo_mComp metacompo_mcomp) {
        this.metacompo_mcomp = metacompo_mcomp;
    }
    public List<metaCompo_mPort> getMetacompo_mports() {
        return metacompo_mports;
    }

    public void addMetacompo_mport(Metacompo_mport metacompo_mport) {
        this.metacompo_mports.add(metacompo_mport);
    }
    public List<metaCompo_mVariable> getMetacompo_mvariables() {
        return metacompo_mvariables;
    }

    public void addMetacompo_mvariable(Metacompo_mvariable metacompo_mvariable) {
        this.metacompo_mvariables.add(metacompo_mvariable);
    }

}