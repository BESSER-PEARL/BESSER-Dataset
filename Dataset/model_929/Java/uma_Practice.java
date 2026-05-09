





import java.util.List;
import java.util.ArrayList;

public class uma_Practice extends Guidance {






    private uma_Practice uma_practice;




    private List<uma_Activity> uma_activitys;




    private List<uma_ContentElement> uma_contentelements;


    public uma_Practice(
    ) {
        super(
        );
        this.uma_activitys = new ArrayList<>();
        this.uma_contentelements = new ArrayList<>();
    }

    public uma_Practice(
        ArrayList<uma_Activity> uma_activitys,        ArrayList<uma_ContentElement> uma_contentelements    ) {
        this.uma_activitys = uma_activitys;
        this.uma_contentelements = uma_contentelements;
    }


    public uma_Practice getUma_practice() {
        return uma_practice;
    }

    public void setUma_practice(uma_Practice uma_practice) {
        this.uma_practice = uma_practice;
    }
    public List<uma_Activity> getUma_activitys() {
        return uma_activitys;
    }

    public void addUma_activity(Uma_activity uma_activity) {
        this.uma_activitys.add(uma_activity);
    }
    public List<uma_ContentElement> getUma_contentelements() {
        return uma_contentelements;
    }

    public void addUma_contentelement(Uma_contentelement uma_contentelement) {
        this.uma_contentelements.add(uma_contentelement);
    }

}