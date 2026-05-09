





import java.util.List;
import java.util.ArrayList;

public class model_task_Milestone extends WorkItem {






    private List<UnicaseModelElement> unicasemodelelements;


    public model_task_Milestone(
    ) {
        super(
        );
        this.unicasemodelelements = new ArrayList<>();
    }

    public model_task_Milestone(
        ArrayList<UnicaseModelElement> unicasemodelelements    ) {
        this.unicasemodelelements = unicasemodelelements;
    }


    public List<UnicaseModelElement> getUnicasemodelelements() {
        return unicasemodelelements;
    }

    public void addUnicasemodelelement(Unicasemodelelement unicasemodelelement) {
        this.unicasemodelelements.add(unicasemodelelement);
    }

}