





import java.util.List;
import java.util.ArrayList;

public class uma_Discipline extends ContentCategory {






    private List<uma_Activity> uma_activitys;




    private List<uma_Task> uma_tasks;


    public uma_Discipline(
    ) {
        super(
        );
        this.uma_activitys = new ArrayList<>();
        this.uma_tasks = new ArrayList<>();
    }

    public uma_Discipline(
        ArrayList<uma_Activity> uma_activitys,        ArrayList<uma_Task> uma_tasks    ) {
        this.uma_activitys = uma_activitys;
        this.uma_tasks = uma_tasks;
    }


    public List<uma_Activity> getUma_activitys() {
        return uma_activitys;
    }

    public void addUma_activity(Uma_activity uma_activity) {
        this.uma_activitys.add(uma_activity);
    }
    public List<uma_Task> getUma_tasks() {
        return uma_tasks;
    }

    public void addUma_task(Uma_task uma_task) {
        this.uma_tasks.add(uma_task);
    }

}