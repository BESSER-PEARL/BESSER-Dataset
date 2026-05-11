





import java.util.List;
import java.util.ArrayList;

public class cal_AstTypeParameterList  {






    private cal_AstType cal_asttype;




    private List<cal_AstTypeParam> cal_asttypeparams;


    public cal_AstTypeParameterList(
    ) {
        this.cal_asttypeparams = new ArrayList<>();
    }

    public cal_AstTypeParameterList(
        ArrayList<cal_AstTypeParam> cal_asttypeparams    ) {
        this.cal_asttypeparams = cal_asttypeparams;
    }


    public cal_AstType getCal_asttype() {
        return cal_asttype;
    }

    public void setCal_asttype(cal_AstType cal_asttype) {
        this.cal_asttype = cal_asttype;
    }
    public List<cal_AstTypeParam> getCal_asttypeparams() {
        return cal_asttypeparams;
    }

    public void addCal_asttypeparam(Cal_asttypeparam cal_asttypeparam) {
        this.cal_asttypeparams.add(cal_asttypeparam);
    }

}