





import java.util.List;
import java.util.ArrayList;

public class cal_AstPort  {

    private String name;





    private List<cal_AstAnnotation> cal_astannotations;




    private cal_AstAbstractActor cal_astabstractactor;




    private cal_AstAbstractActor cal_astabstractactor;


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

    public List<cal_AstAnnotation> getCal_astannotations() {
        return cal_astannotations;
    }

    public void addCal_astannotation(Cal_astannotation cal_astannotation) {
        this.cal_astannotations.add(cal_astannotation);
    }
    public cal_AstAbstractActor getCal_astabstractactor() {
        return cal_astabstractactor;
    }

    public void setCal_astabstractactor(cal_AstAbstractActor cal_astabstractactor) {
        this.cal_astabstractactor = cal_astabstractactor;
    }
    public cal_AstAbstractActor getCal_astabstractactor() {
        return cal_astabstractactor;
    }

    public void setCal_astabstractactor(cal_AstAbstractActor cal_astabstractactor) {
        this.cal_astabstractactor = cal_astabstractactor;
    }

}