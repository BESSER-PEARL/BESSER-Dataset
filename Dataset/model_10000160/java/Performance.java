





import java.util.List;
import java.util.ArrayList;

public class Performance  {

    private String Name;
    private String Target;
    private String Punctuality;
    private String Coordination;



    public Performance(
        String Name,        String Target,        String Punctuality,        String Coordination    ) {
        this.Name = Name;
        this.Target = Target;
        this.Punctuality = Punctuality;
        this.Coordination = Coordination;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getTarget() {
        return Target;
    }

    public void setTarget(String Target) {
        this.Target = Target;
    }
    public String getPunctuality() {
        return Punctuality;
    }

    public void setPunctuality(String Punctuality) {
        this.Punctuality = Punctuality;
    }
    public String getCoordination() {
        return Coordination;
    }

    public void setCoordination(String Coordination) {
        this.Coordination = Coordination;
    }


}