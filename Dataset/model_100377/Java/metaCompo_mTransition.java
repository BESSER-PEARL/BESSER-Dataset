





import java.util.List;
import java.util.ArrayList;

public class metaCompo_mTransition  {

    private String guard;
    private String triggerExp;
    private String name;
    private String action;





    private List<metaCompo_mPort> metacompo_mports;




    private List<metaCompo_mVariable> metacompo_mvariables;




    private metaCompo_mState metacompo_mstate;




    private metaCompo_mState metacompo_mstate;




    private metaCompo_mState metacompo_mstate;




    private metaCompo_mState metacompo_mstate;


    public metaCompo_mTransition(
        String guard,        String triggerExp,        String name,        String action    ) {
        this.guard = guard;
        this.triggerExp = triggerExp;
        this.name = name;
        this.action = action;
        this.metacompo_mports = new ArrayList<>();
        this.metacompo_mvariables = new ArrayList<>();
    }

    public metaCompo_mTransition(
        String guard,        String triggerExp,        String name,        String action        ArrayList<metaCompo_mPort> metacompo_mports,        ArrayList<metaCompo_mVariable> metacompo_mvariables    ) {
        this.guard = guard;
        this.triggerExp = triggerExp;
        this.name = name;
        this.action = action;
        this.metacompo_mports = metacompo_mports;
        this.metacompo_mvariables = metacompo_mvariables;
    }

    public String getGuard() {
        return guard;
    }

    public void setGuard(String guard) {
        this.guard = guard;
    }
    public String getTriggerexp() {
        return triggerExp;
    }

    public void setTriggerexp(String triggerExp) {
        this.triggerExp = triggerExp;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
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
    public metaCompo_mState getMetacompo_mstate() {
        return metacompo_mstate;
    }

    public void setMetacompo_mstate(metaCompo_mState metacompo_mstate) {
        this.metacompo_mstate = metacompo_mstate;
    }
    public metaCompo_mState getMetacompo_mstate() {
        return metacompo_mstate;
    }

    public void setMetacompo_mstate(metaCompo_mState metacompo_mstate) {
        this.metacompo_mstate = metacompo_mstate;
    }
    public metaCompo_mState getMetacompo_mstate() {
        return metacompo_mstate;
    }

    public void setMetacompo_mstate(metaCompo_mState metacompo_mstate) {
        this.metacompo_mstate = metacompo_mstate;
    }
    public metaCompo_mState getMetacompo_mstate() {
        return metacompo_mstate;
    }

    public void setMetacompo_mstate(metaCompo_mState metacompo_mstate) {
        this.metacompo_mstate = metacompo_mstate;
    }

}