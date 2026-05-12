





import java.util.List;
import java.util.ArrayList;

public class umlState_EntryRule  {

    private String behaviorName;
    private String kind;





    private umlState_StateRule umlstate_staterule;


    public umlState_EntryRule(
        String behaviorName,        String kind    ) {
        this.behaviorName = behaviorName;
        this.kind = kind;
    }


    public String getBehaviorname() {
        return behaviorName;
    }

    public void setBehaviorname(String behaviorName) {
        this.behaviorName = behaviorName;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public umlState_StateRule getUmlstate_staterule() {
        return umlstate_staterule;
    }

    public void setUmlstate_staterule(umlState_StateRule umlstate_staterule) {
        this.umlstate_staterule = umlstate_staterule;
    }

}