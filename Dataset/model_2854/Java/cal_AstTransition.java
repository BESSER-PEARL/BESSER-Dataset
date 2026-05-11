





import java.util.List;
import java.util.ArrayList;

public class cal_AstTransition  {






    private List<cal_AstTag> cal_asttags;




    private cal_AstSchedule cal_astschedule;




    private cal_AstState cal_aststate;




    private cal_AstState cal_aststate;


    public cal_AstTransition(
    ) {
        this.cal_asttags = new ArrayList<>();
    }

    public cal_AstTransition(
        ArrayList<cal_AstTag> cal_asttags    ) {
        this.cal_asttags = cal_asttags;
    }


    public List<cal_AstTag> getCal_asttags() {
        return cal_asttags;
    }

    public void addCal_asttag(Cal_asttag cal_asttag) {
        this.cal_asttags.add(cal_asttag);
    }
    public cal_AstSchedule getCal_astschedule() {
        return cal_astschedule;
    }

    public void setCal_astschedule(cal_AstSchedule cal_astschedule) {
        this.cal_astschedule = cal_astschedule;
    }
    public cal_AstState getCal_aststate() {
        return cal_aststate;
    }

    public void setCal_aststate(cal_AstState cal_aststate) {
        this.cal_aststate = cal_aststate;
    }
    public cal_AstState getCal_aststate() {
        return cal_aststate;
    }

    public void setCal_aststate(cal_AstState cal_aststate) {
        this.cal_aststate = cal_aststate;
    }

}