





import java.util.List;
import java.util.ArrayList;

public class gsml_Grade  {

    private String Name;
    private float RequiredPoints;





    private gsml_GradingScheme gsml_gradingscheme;




    private gsml_GradingScheme gsml_gradingscheme;


    public gsml_Grade(
        String Name,        float RequiredPoints    ) {
        this.Name = Name;
        this.RequiredPoints = RequiredPoints;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public float getRequiredpoints() {
        return RequiredPoints;
    }

    public void setRequiredpoints(float RequiredPoints) {
        this.RequiredPoints = RequiredPoints;
    }

    public gsml_GradingScheme getGsml_gradingscheme() {
        return gsml_gradingscheme;
    }

    public void setGsml_gradingscheme(gsml_GradingScheme gsml_gradingscheme) {
        this.gsml_gradingscheme = gsml_gradingscheme;
    }
    public gsml_GradingScheme getGsml_gradingscheme() {
        return gsml_gradingscheme;
    }

    public void setGsml_gradingscheme(gsml_GradingScheme gsml_gradingscheme) {
        this.gsml_gradingscheme = gsml_gradingscheme;
    }

}