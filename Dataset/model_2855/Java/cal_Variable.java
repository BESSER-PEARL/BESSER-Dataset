





import java.util.List;
import java.util.ArrayList;

public class cal_Variable  {

    private String name;
    private boolean constant;





    private cal_AstProcedure cal_astprocedure;




    private cal_Function cal_function;




    private cal_Function cal_function;




    private cal_AstProcedure cal_astprocedure;




    private List<cal_AstAnnotation> cal_astannotations;




    private cal_AstUnit cal_astunit;




    private cal_AstActor cal_astactor;




    private cal_AstActor cal_astactor;


    public cal_Variable(
        String name,        boolean constant    ) {
        this.name = name;
        this.constant = constant;
        this.cal_astannotations = new ArrayList<>();
    }

    public cal_Variable(
        String name,        boolean constant        ArrayList<cal_AstAnnotation> cal_astannotations    ) {
        this.name = name;
        this.constant = constant;
        this.cal_astannotations = cal_astannotations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getConstant() {
        return constant;
    }

    public void setConstant(boolean constant) {
        this.constant = constant;
    }

    public cal_AstProcedure getCal_astprocedure() {
        return cal_astprocedure;
    }

    public void setCal_astprocedure(cal_AstProcedure cal_astprocedure) {
        this.cal_astprocedure = cal_astprocedure;
    }
    public cal_Function getCal_function() {
        return cal_function;
    }

    public void setCal_function(cal_Function cal_function) {
        this.cal_function = cal_function;
    }
    public cal_Function getCal_function() {
        return cal_function;
    }

    public void setCal_function(cal_Function cal_function) {
        this.cal_function = cal_function;
    }
    public cal_AstProcedure getCal_astprocedure() {
        return cal_astprocedure;
    }

    public void setCal_astprocedure(cal_AstProcedure cal_astprocedure) {
        this.cal_astprocedure = cal_astprocedure;
    }
    public List<cal_AstAnnotation> getCal_astannotations() {
        return cal_astannotations;
    }

    public void addCal_astannotation(Cal_astannotation cal_astannotation) {
        this.cal_astannotations.add(cal_astannotation);
    }
    public cal_AstUnit getCal_astunit() {
        return cal_astunit;
    }

    public void setCal_astunit(cal_AstUnit cal_astunit) {
        this.cal_astunit = cal_astunit;
    }
    public cal_AstActor getCal_astactor() {
        return cal_astactor;
    }

    public void setCal_astactor(cal_AstActor cal_astactor) {
        this.cal_astactor = cal_astactor;
    }
    public cal_AstActor getCal_astactor() {
        return cal_astactor;
    }

    public void setCal_astactor(cal_AstActor cal_astactor) {
        this.cal_astactor = cal_astactor;
    }

}