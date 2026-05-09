





import java.util.List;
import java.util.ArrayList;

public class uma_Practice extends Guidance {






    private List<uma_ContentElement> uma_contentelements;




    private List<uma_Practice> uma_practices;




    private List<uma_Activity> uma_activitys;


    public uma_Practice(
    ) {
        super(
        );
        this.uma_contentelements = new ArrayList<>();
        this.uma_practices = new ArrayList<>();
        this.uma_activitys = new ArrayList<>();
    }

    public uma_Practice(
        ArrayList<uma_ContentElement> uma_contentelements,        ArrayList<uma_Practice> uma_practices,        ArrayList<uma_Activity> uma_activitys    ) {
        this.uma_contentelements = uma_contentelements;
        this.uma_practices = uma_practices;
        this.uma_activitys = uma_activitys;
    }


    public List<uma_ContentElement> getUma_contentelements() {
        return uma_contentelements;
    }

    public void addUma_contentelement(Uma_contentelement uma_contentelement) {
        this.uma_contentelements.add(uma_contentelement);
    }
    public List<uma_Practice> getUma_practices() {
        return uma_practices;
    }

    public void addUma_practice(Uma_practice uma_practice) {
        this.uma_practices.add(uma_practice);
    }
    public List<uma_Activity> getUma_activitys() {
        return uma_activitys;
    }

    public void addUma_activity(Uma_activity uma_activity) {
        this.uma_activitys.add(uma_activity);
    }

}