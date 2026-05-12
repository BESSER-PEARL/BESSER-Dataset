





import java.util.List;
import java.util.ArrayList;

public class umlState_ExitRule  {

    private String kind;
    private String behaviorName;



    public umlState_ExitRule(
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


}