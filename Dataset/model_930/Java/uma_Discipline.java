





import java.util.List;
import java.util.ArrayList;

public class uma_Discipline extends ContentCategory {






    private List<uma_Discipline> uma_disciplines;




    private List<uma_Activity> uma_activitys;


    public uma_Discipline(
    ) {
        super(
        );
        this.uma_disciplines = new ArrayList<>();
        this.uma_activitys = new ArrayList<>();
    }

    public uma_Discipline(
        ArrayList<uma_Discipline> uma_disciplines,        ArrayList<uma_Activity> uma_activitys    ) {
        this.uma_disciplines = uma_disciplines;
        this.uma_activitys = uma_activitys;
    }


    public List<uma_Discipline> getUma_disciplines() {
        return uma_disciplines;
    }

    public void addUma_discipline(Uma_discipline uma_discipline) {
        this.uma_disciplines.add(uma_discipline);
    }
    public List<uma_Activity> getUma_activitys() {
        return uma_activitys;
    }

    public void addUma_activity(Uma_activity uma_activity) {
        this.uma_activitys.add(uma_activity);
    }

}