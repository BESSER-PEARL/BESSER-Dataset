





import java.util.List;
import java.util.ArrayList;

public class cal_Statement  {






    private cal_AstAction cal_astaction;




    private List<cal_AstAnnotation> cal_astannotations;




    private cal_AstProcedure cal_astprocedure;


    public cal_Statement(
    ) {
        this.cal_astannotations = new ArrayList<>();
    }

    public cal_Statement(
        ArrayList<cal_AstAnnotation> cal_astannotations    ) {
        this.cal_astannotations = cal_astannotations;
    }


    public cal_AstAction getCal_astaction() {
        return cal_astaction;
    }

    public void setCal_astaction(cal_AstAction cal_astaction) {
        this.cal_astaction = cal_astaction;
    }
    public List<cal_AstAnnotation> getCal_astannotations() {
        return cal_astannotations;
    }

    public void addCal_astannotation(Cal_astannotation cal_astannotation) {
        this.cal_astannotations.add(cal_astannotation);
    }
    public cal_AstProcedure getCal_astprocedure() {
        return cal_astprocedure;
    }

    public void setCal_astprocedure(cal_AstProcedure cal_astprocedure) {
        this.cal_astprocedure = cal_astprocedure;
    }

}