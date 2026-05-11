





import java.util.List;
import java.util.ArrayList;

public class courses_EvaluationForm  {

    private String examAids;
    private String duration;
    private String type;
    private String weighting;



    public courses_EvaluationForm(
        String examAids,        String duration,        String type,        String weighting    ) {
        this.examAids = examAids;
        this.duration = duration;
        this.type = type;
        this.weighting = weighting;
    }


    public String getExamaids() {
        return examAids;
    }

    public void setExamaids(String examAids) {
        this.examAids = examAids;
    }
    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getWeighting() {
        return weighting;
    }

    public void setWeighting(String weighting) {
        this.weighting = weighting;
    }


}