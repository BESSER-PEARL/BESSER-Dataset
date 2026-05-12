





import java.util.List;
import java.util.ArrayList;

public class umlTransition_EffectRule  {

    private String kind;
    private String behaviorName;





    private umlTransition_TransitionRule umltransition_transitionrule;


    public umlTransition_EffectRule(
        String kind,        String behaviorName    ) {
        this.kind = kind;
        this.behaviorName = behaviorName;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getBehaviorname() {
        return behaviorName;
    }

    public void setBehaviorname(String behaviorName) {
        this.behaviorName = behaviorName;
    }

    public umlTransition_TransitionRule getUmltransition_transitionrule() {
        return umltransition_transitionrule;
    }

    public void setUmltransition_transitionrule(umlTransition_TransitionRule umltransition_transitionrule) {
        this.umltransition_transitionrule = umltransition_transitionrule;
    }

}