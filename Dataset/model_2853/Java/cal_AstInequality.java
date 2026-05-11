





import java.util.List;
import java.util.ArrayList;

public class cal_AstInequality  {






    private List<cal_AstTag> cal_asttags;




    private cal_AstPriority cal_astpriority;


    public cal_AstInequality(
    ) {
        this.cal_asttags = new ArrayList<>();
    }

    public cal_AstInequality(
        ArrayList<cal_AstTag> cal_asttags    ) {
        this.cal_asttags = cal_asttags;
    }


    public List<cal_AstTag> getCal_asttags() {
        return cal_asttags;
    }

    public void addCal_asttag(Cal_asttag cal_asttag) {
        this.cal_asttags.add(cal_asttag);
    }
    public cal_AstPriority getCal_astpriority() {
        return cal_astpriority;
    }

    public void setCal_astpriority(cal_AstPriority cal_astpriority) {
        this.cal_astpriority = cal_astpriority;
    }

}