





import java.util.List;
import java.util.ArrayList;

public class shr5_Drug extends Substance, Modifizierbar {

    private String addictionType;
    private String duration;



    public shr5_Drug(
        String addictionType,        String duration    ) {
        super(
        );
        this.addictionType = addictionType;
        this.duration = duration;
    }


    public String getAddictiontype() {
        return addictionType;
    }

    public void setAddictiontype(String addictionType) {
        this.addictionType = addictionType;
    }
    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }


}