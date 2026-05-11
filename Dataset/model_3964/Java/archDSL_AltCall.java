





import java.util.List;
import java.util.ArrayList;

public class archDSL_AltCall extends SuperCall {

    private boolean opt;





    private List<archDSL_SuperMethod> archdsl_supermethods;


    public archDSL_AltCall(
        boolean opt    ) {
        super(
        );
        this.opt = opt;
        this.archdsl_supermethods = new ArrayList<>();
    }

    public archDSL_AltCall(
        boolean opt        ArrayList<archDSL_SuperMethod> archdsl_supermethods    ) {
        this.opt = opt;
        this.archdsl_supermethods = archdsl_supermethods;
    }

    public boolean getOpt() {
        return opt;
    }

    public void setOpt(boolean opt) {
        this.opt = opt;
    }

    public List<archDSL_SuperMethod> getArchdsl_supermethods() {
        return archdsl_supermethods;
    }

    public void addArchdsl_supermethod(Archdsl_supermethod archdsl_supermethod) {
        this.archdsl_supermethods.add(archdsl_supermethod);
    }

}