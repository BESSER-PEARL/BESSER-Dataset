





import java.util.List;
import java.util.ArrayList;

public class cal_AstActorVariable  {

    private String name;





    private List<cal_AstAssignParameter> cal_astassignparameters;




    private cal_AstNetwork cal_astnetwork;




    private cal_AstEntity cal_astentity;


    public cal_AstActorVariable(
        String name    ) {
        this.name = name;
        this.cal_astassignparameters = new ArrayList<>();
    }

    public cal_AstActorVariable(
        String name        ArrayList<cal_AstAssignParameter> cal_astassignparameters    ) {
        this.name = name;
        this.cal_astassignparameters = cal_astassignparameters;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<cal_AstAssignParameter> getCal_astassignparameters() {
        return cal_astassignparameters;
    }

    public void addCal_astassignparameter(Cal_astassignparameter cal_astassignparameter) {
        this.cal_astassignparameters.add(cal_astassignparameter);
    }
    public cal_AstNetwork getCal_astnetwork() {
        return cal_astnetwork;
    }

    public void setCal_astnetwork(cal_AstNetwork cal_astnetwork) {
        this.cal_astnetwork = cal_astnetwork;
    }
    public cal_AstEntity getCal_astentity() {
        return cal_astentity;
    }

    public void setCal_astentity(cal_AstEntity cal_astentity) {
        this.cal_astentity = cal_astentity;
    }

}