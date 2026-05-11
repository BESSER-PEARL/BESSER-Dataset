





import java.util.List;
import java.util.ArrayList;

public class cal_AstProcedure extends AstExternalProcedure {

    private String name;





    private List<cal_AstVariable> cal_astvariables;




    private List<cal_AstAnnotation> cal_astannotations;




    private cal_AstActor cal_astactor;




    private List<cal_AstVariable> cal_astvariables;


    public cal_AstProcedure(
        String name    ) {
        super(
        );
        this.name = name;
        this.cal_astvariables = new ArrayList<>();
        this.cal_astannotations = new ArrayList<>();
        this.cal_astvariables = new ArrayList<>();
    }

    public cal_AstProcedure(
        String name        ArrayList<cal_AstVariable> cal_astvariables,        ArrayList<cal_AstAnnotation> cal_astannotations,        ArrayList<cal_AstVariable> cal_astvariables    ) {
        this.name = name;
        this.cal_astvariables = cal_astvariables;
        this.cal_astannotations = cal_astannotations;
        this.cal_astvariables = cal_astvariables;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<cal_AstVariable> getCal_astvariables() {
        return cal_astvariables;
    }

    public void addCal_astvariable(Cal_astvariable cal_astvariable) {
        this.cal_astvariables.add(cal_astvariable);
    }
    public List<cal_AstAnnotation> getCal_astannotations() {
        return cal_astannotations;
    }

    public void addCal_astannotation(Cal_astannotation cal_astannotation) {
        this.cal_astannotations.add(cal_astannotation);
    }
    public cal_AstActor getCal_astactor() {
        return cal_astactor;
    }

    public void setCal_astactor(cal_AstActor cal_astactor) {
        this.cal_astactor = cal_astactor;
    }
    public List<cal_AstVariable> getCal_astvariables() {
        return cal_astvariables;
    }

    public void addCal_astvariable(Cal_astvariable cal_astvariable) {
        this.cal_astvariables.add(cal_astvariable);
    }

}