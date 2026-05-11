





import java.util.List;
import java.util.ArrayList;

public class cal_AstPriority  {






    private cal_AstActor cal_astactor;




    private List<cal_AstInequality> cal_astinequalitys;


    public cal_AstPriority(
    ) {
        this.cal_astinequalitys = new ArrayList<>();
    }

    public cal_AstPriority(
        ArrayList<cal_AstInequality> cal_astinequalitys    ) {
        this.cal_astinequalitys = cal_astinequalitys;
    }


    public cal_AstActor getCal_astactor() {
        return cal_astactor;
    }

    public void setCal_astactor(cal_AstActor cal_astactor) {
        this.cal_astactor = cal_astactor;
    }
    public List<cal_AstInequality> getCal_astinequalitys() {
        return cal_astinequalitys;
    }

    public void addCal_astinequality(Cal_astinequality cal_astinequality) {
        this.cal_astinequalitys.add(cal_astinequality);
    }

}