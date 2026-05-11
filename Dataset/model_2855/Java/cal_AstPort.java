





import java.util.List;
import java.util.ArrayList;

public class cal_AstPort  {

    private String name;





    private cal_AstActor cal_astactor;




    private List<cal_AstAnnotation> cal_astannotations;




    private cal_AstActor cal_astactor;




    private cal_AstType cal_asttype;


    public cal_AstPort(
        String name    ) {
        this.name = name;
        this.cal_astannotations = new ArrayList<>();
    }

    public cal_AstPort(
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
    public cal_AstType getCal_asttype() {
        return cal_asttype;
    }

    public void setCal_asttype(cal_AstType cal_asttype) {
        this.cal_asttype = cal_asttype;
    }

}