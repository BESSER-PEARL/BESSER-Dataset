





import java.util.List;
import java.util.ArrayList;

public class cal_Inequality  {






    private cal_Priority cal_priority;




    private List<cal_AstTag> cal_asttags;


    public cal_Inequality(
    ) {
        this.cal_asttags = new ArrayList<>();
    }

    public cal_Inequality(
        ArrayList<cal_AstTag> cal_asttags    ) {
        this.cal_asttags = cal_asttags;
    }


    public cal_Priority getCal_priority() {
        return cal_priority;
    }

    public void setCal_priority(cal_Priority cal_priority) {
        this.cal_priority = cal_priority;
    }
    public List<cal_AstTag> getCal_asttags() {
        return cal_asttags;
    }

    public void addCal_asttag(Cal_asttag cal_asttag) {
        this.cal_asttags.add(cal_asttag);
    }

}