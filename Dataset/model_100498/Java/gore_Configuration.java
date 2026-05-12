





import java.util.List;
import java.util.ArrayList;

public class gore_Configuration  {






    private gore_GoalModel gore_goalmodel;




    private gore_Parameter gore_parameter;




    private gore_GoalModel gore_goalmodel;




    private List<gore_Parameter> gore_parameters;


    public gore_Configuration(
    ) {
        this.gore_parameters = new ArrayList<>();
    }

    public gore_Configuration(
        ArrayList<gore_Parameter> gore_parameters    ) {
        this.gore_parameters = gore_parameters;
    }


    public gore_GoalModel getGore_goalmodel() {
        return gore_goalmodel;
    }

    public void setGore_goalmodel(gore_GoalModel gore_goalmodel) {
        this.gore_goalmodel = gore_goalmodel;
    }
    public gore_Parameter getGore_parameter() {
        return gore_parameter;
    }

    public void setGore_parameter(gore_Parameter gore_parameter) {
        this.gore_parameter = gore_parameter;
    }
    public gore_GoalModel getGore_goalmodel() {
        return gore_goalmodel;
    }

    public void setGore_goalmodel(gore_GoalModel gore_goalmodel) {
        this.gore_goalmodel = gore_goalmodel;
    }
    public List<gore_Parameter> getGore_parameters() {
        return gore_parameters;
    }

    public void addGore_parameter(Gore_parameter gore_parameter) {
        this.gore_parameters.add(gore_parameter);
    }

}