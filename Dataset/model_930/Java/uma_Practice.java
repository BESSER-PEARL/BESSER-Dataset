





import java.util.List;
import java.util.ArrayList;

public class uma_Practice extends Guidance {






    private List<uma_Activity> uma_activitys;




    private List<uma_Practice> uma_practices;


    public uma_Practice(
    ) {
        super(
        );
        this.uma_activitys = new ArrayList<>();
        this.uma_practices = new ArrayList<>();
    }

    public uma_Practice(
        ArrayList<uma_Activity> uma_activitys,        ArrayList<uma_Practice> uma_practices    ) {
        this.uma_activitys = uma_activitys;
        this.uma_practices = uma_practices;
    }


    public List<uma_Activity> getUma_activitys() {
        return uma_activitys;
    }

    public void addUma_activity(Uma_activity uma_activity) {
        this.uma_activitys.add(uma_activity);
    }
    public List<uma_Practice> getUma_practices() {
        return uma_practices;
    }

    public void addUma_practice(Uma_practice uma_practice) {
        this.uma_practices.add(uma_practice);
    }

}