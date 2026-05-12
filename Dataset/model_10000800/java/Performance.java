





import java.util.List;
import java.util.ArrayList;

public class Performance  {

    private String Punctuality;
    private String Coordination;
    private String Name;
    private String Target;



    public Performance(
        String Punctuality,        String Coordination,        String Name,        String Target    ) {
        this.Punctuality = Punctuality;
        this.Coordination = Coordination;
        this.Name = Name;
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


}