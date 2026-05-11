





import java.util.List;
import java.util.ArrayList;

public class behavioral_status_and_action_old_SAMDerivator  {

    private String kind;





    private SapClass sapclass;


    public behavioral_status_and_action_old_SAMDerivator(
        String kind    ) {
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public SapClass getSapclass() {
        return sapclass;
    }

    public void setSapclass(SapClass sapclass) {
        this.sapclass = sapclass;
    }

}