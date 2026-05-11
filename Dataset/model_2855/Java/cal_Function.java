





import java.util.List;
import java.util.ArrayList;

public class cal_Function  {

    private String name;





    private cal_AstActor cal_astactor;




    private cal_AstUnit cal_astunit;




    private List<cal_AstAnnotation> cal_astannotations;


    public cal_Function(
        String name    ) {
        this.name = name;
        this.cal_astannotations = new ArrayList<>();
    }

    public cal_Function(
        String name        ArrayList<cal_AstAnnotation> cal_astannotations    ) {
        this.name = name;
        this.cal_astannotations = cal_astannotations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cal_AstActor getCal_astactor() {
        return cal_astactor;
    }

    public void setCal_astactor(cal_AstActor cal_astactor) {
        this.cal_astactor = cal_astactor;
    }
    public cal_AstUnit getCal_astunit() {
        return cal_astunit;
    }

    public void setCal_astunit(cal_AstUnit cal_astunit) {
        this.cal_astunit = cal_astunit;
    }
    public List<cal_AstAnnotation> getCal_astannotations() {
        return cal_astannotations;
    }

    public void addCal_astannotation(Cal_astannotation cal_astannotation) {
        this.cal_astannotations.add(cal_astannotation);
    }

}