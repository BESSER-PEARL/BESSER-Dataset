





import java.util.List;
import java.util.ArrayList;

public class uma_Practice extends Guidance {

    private String group2;
    private String contentReference;
    private String activityReference;





    private uma_Practice uma_practice;


    public uma_Practice(
        String group2,        String contentReference,        String activityReference    ) {
        super(
        );
        this.group2 = group2;
        this.contentReference = contentReference;
        this.activityReference = activityReference;
    }


    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }
    public String getContentreference() {
        return contentReference;
    }

    public void setContentreference(String contentReference) {
        this.contentReference = contentReference;
    }
    public String getActivityreference() {
        return activityReference;
    }

    public void setActivityreference(String activityReference) {
        this.activityReference = activityReference;
    }

    public uma_Practice getUma_practice() {
        return uma_practice;
    }

    public void setUma_practice(uma_Practice uma_practice) {
        this.uma_practice = uma_practice;
    }

}