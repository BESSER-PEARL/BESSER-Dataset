





import java.util.List;
import java.util.ArrayList;

public class uma_DisciplineGrouping extends ContentCategory {






    private List<uma_Discipline> uma_disciplines;


    public uma_DisciplineGrouping(
    ) {
        super(
        );
        this.uma_disciplines = new ArrayList<>();
    }

    public uma_DisciplineGrouping(
        ArrayList<uma_Discipline> uma_disciplines    ) {
        this.uma_disciplines = uma_disciplines;
    }


    public List<uma_Discipline> getUma_disciplines() {
        return uma_disciplines;
    }

    public void addUma_discipline(Uma_discipline uma_discipline) {
        this.uma_disciplines.add(uma_discipline);
    }

}