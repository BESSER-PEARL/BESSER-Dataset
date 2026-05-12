





import java.util.List;
import java.util.ArrayList;

public class umlTransition_EffectRule  {

    private String behaviorName;
    private String kind;



    public umlTransition_EffectRule(
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


}