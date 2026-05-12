





import java.util.List;
import java.util.ArrayList;

public class Performance  {

    private String Punctuality;
    private String Name;
    private String Coordination;
    private String Target;



    public Performance(
        String Punctuality,        String Name,        String Coordination,        String Target    ) {
        this.Punctuality = Punctuality;
        this.Name = Name;
        this.Coordination = Coordination;
        this.Target = Target;
    }


    public String getPunctuality() {
        return Punctuality;
    }

    public void setPunctuality(String Punctuality) {
        this.Punctuality = Punctuality;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getCoordination() {
        return Coordination;
    }

    public void setCoordination(String Coordination) {
        this.Coordination = Coordination;
    }
    public String getTarget() {
        return Target;
    }

    public void setTarget(String Target) {
        this.Target = Target;
    }


}