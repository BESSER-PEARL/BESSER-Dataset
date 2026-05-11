





import java.util.List;
import java.util.ArrayList;

public class cal_AstAbstractActor  {

    private String name;





    private cal_AstEntity cal_astentity;




    private List<cal_AstVariable> cal_astvariables;


    public cal_AstAbstractActor(
        String name    ) {
        this.name = name;
        this.cal_astvariables = new ArrayList<>();
    }

    public cal_AstAbstractActor(
        String name        ArrayList<cal_AstVariable> cal_astvariables    ) {
        this.name = name;
        this.cal_astvariables = cal_astvariables;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cal_AstEntity getCal_astentity() {
        return cal_astentity;
    }

    public void setCal_astentity(cal_AstEntity cal_astentity) {
        this.cal_astentity = cal_astentity;
    }
    public List<cal_AstVariable> getCal_astvariables() {
        return cal_astvariables;
    }

    public void addCal_astvariable(Cal_astvariable cal_astvariable) {
        this.cal_astvariables.add(cal_astvariable);
    }

}