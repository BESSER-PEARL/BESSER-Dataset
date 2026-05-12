





import java.util.List;
import java.util.ArrayList;

public class metaCompo_mState  {

    private String name;





    private List<metaCompo_mVariable> metacompo_mvariables;




    private metaCompo_mFSM metacompo_mfsm;




    private metaCompo_mFSM metacompo_mfsm;




    private metaCompo_mFSM metacompo_mfsm;




    private List<metaCompo_mState> metacompo_mstates;




    private metaCompo_mFSM metacompo_mfsm;


    public metaCompo_mState(
        String name    ) {
        this.name = name;
        this.metacompo_mvariables = new ArrayList<>();
        this.metacompo_mstates = new ArrayList<>();
    }

    public metaCompo_mState(
        String name        ArrayList<metaCompo_mVariable> metacompo_mvariables,        ArrayList<metaCompo_mState> metacompo_mstates    ) {
        this.name = name;
        this.metacompo_mvariables = metacompo_mvariables;
        this.metacompo_mstates = metacompo_mstates;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<metaCompo_mVariable> getMetacompo_mvariables() {
        return metacompo_mvariables;
    }

    public void addMetacompo_mvariable(Metacompo_mvariable metacompo_mvariable) {
        this.metacompo_mvariables.add(metacompo_mvariable);
    }
    public metaCompo_mFSM getMetacompo_mfsm() {
        return metacompo_mfsm;
    }

    public void setMetacompo_mfsm(metaCompo_mFSM metacompo_mfsm) {
        this.metacompo_mfsm = metacompo_mfsm;
    }
    public metaCompo_mFSM getMetacompo_mfsm() {
        return metacompo_mfsm;
    }

    public void setMetacompo_mfsm(metaCompo_mFSM metacompo_mfsm) {
        this.metacompo_mfsm = metacompo_mfsm;
    }
    public metaCompo_mFSM getMetacompo_mfsm() {
        return metacompo_mfsm;
    }

    public void setMetacompo_mfsm(metaCompo_mFSM metacompo_mfsm) {
        this.metacompo_mfsm = metacompo_mfsm;
    }
    public List<metaCompo_mState> getMetacompo_mstates() {
        return metacompo_mstates;
    }

    public void addMetacompo_mstate(Metacompo_mstate metacompo_mstate) {
        this.metacompo_mstates.add(metacompo_mstate);
    }
    public metaCompo_mFSM getMetacompo_mfsm() {
        return metacompo_mfsm;
    }

    public void setMetacompo_mfsm(metaCompo_mFSM metacompo_mfsm) {
        this.metacompo_mfsm = metacompo_mfsm;
    }

}