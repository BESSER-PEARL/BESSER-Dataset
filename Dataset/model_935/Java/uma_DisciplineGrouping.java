





import java.util.List;
import java.util.ArrayList;

public class uma_DisciplineGrouping extends ContentCategory {

    private String group2;
    private String discipline;



    public uma_DisciplineGrouping(
        String group2,        String discipline    ) {
        super(
        );
        this.group2 = group2;
        this.discipline = discipline;
    }


    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }
    public String getDiscipline() {
        return discipline;
    }

    public void setDiscipline(String discipline) {
        this.discipline = discipline;
    }


}