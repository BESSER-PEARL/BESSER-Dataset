





import java.util.List;
import java.util.ArrayList;

public class MARTE_Library_GRM_BasicTypes_PeriodicServerParameters extends FixedPriorityParameters {

    private String backgroundPriority;
    private String kind;



    public MARTE_Library_GRM_BasicTypes_PeriodicServerParameters(
        String backgroundPriority,        String kind    ) {
        super(
        );
        this.backgroundPriority = backgroundPriority;
        this.kind = kind;
    }


    public String getBackgroundpriority() {
        return backgroundPriority;
    }

    public void setBackgroundpriority(String backgroundPriority) {
        this.backgroundPriority = backgroundPriority;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}