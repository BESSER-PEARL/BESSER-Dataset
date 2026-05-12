





import java.util.List;
import java.util.ArrayList;

public class FSmachine_Root  {

    private String FSmachineName;





    private List<FSmachine_AbstractConection> fsmachine_abstractconections;




    private FSmachine_AbstractConection fsmachine_abstractconection;


    public FSmachine_Root(
        String FSmachineName    ) {
        this.FSmachineName = FSmachineName;
        this.fsmachine_abstractconections = new ArrayList<>();
    }

    public FSmachine_Root(
        String FSmachineName        ArrayList<FSmachine_AbstractConection> fsmachine_abstractconections    ) {
        this.FSmachineName = FSmachineName;
        this.fsmachine_abstractconections = fsmachine_abstractconections;
    }

    public String getFsmachinename() {
        return FSmachineName;
    }

    public void setFsmachinename(String FSmachineName) {
        this.FSmachineName = FSmachineName;
    }

    public List<FSmachine_AbstractConection> getFsmachine_abstractconections() {
        return fsmachine_abstractconections;
    }

    public void addFsmachine_abstractconection(Fsmachine_abstractconection fsmachine_abstractconection) {
        this.fsmachine_abstractconections.add(fsmachine_abstractconection);
    }
    public FSmachine_AbstractConection getFsmachine_abstractconection() {
        return fsmachine_abstractconection;
    }

    public void setFsmachine_abstractconection(FSmachine_AbstractConection fsmachine_abstractconection) {
        this.fsmachine_abstractconection = fsmachine_abstractconection;
    }

}