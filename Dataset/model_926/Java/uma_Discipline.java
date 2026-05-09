





import java.util.List;
import java.util.ArrayList;

public class uma_Discipline extends ContentCategory {






    private uma_Discipline uma_discipline;




    private List<uma_Task> uma_tasks;




    private List<uma_Activity> uma_activitys;


    public uma_Discipline(
    ) {
        super(
        );
        this.uma_tasks = new ArrayList<>();
        this.uma_activitys = new ArrayList<>();
    }

    public uma_Discipline(
        ArrayList<uma_Task> uma_tasks,        ArrayList<uma_Activity> uma_activitys    ) {
        this.uma_tasks = uma_tasks;
        this.uma_activitys = uma_activitys;
    }


    public uma_Discipline getUma_discipline() {
        return uma_discipline;
    }

    public void setUma_discipline(uma_Discipline uma_discipline) {
        this.uma_discipline = uma_discipline;
    }
    public List<uma_Task> getUma_tasks() {
        return uma_tasks;
    }

    public void addUma_task(Uma_task uma_task) {
        this.uma_tasks.add(uma_task);
    }
    public List<uma_Activity> getUma_activitys() {
        return uma_activitys;
    }

    public void addUma_activity(Uma_activity uma_activity) {
        this.uma_activitys.add(uma_activity);
    }

}