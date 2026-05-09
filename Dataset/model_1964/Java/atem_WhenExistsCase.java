





import java.util.List;
import java.util.ArrayList;

public class atem_WhenExistsCase  {






    private atem_Definition atem_definition;




    private List<atem_AbstractComponent> atem_abstractcomponents;




    private atem_WhenExists atem_whenexists;


    public atem_WhenExistsCase(
    ) {
        this.atem_abstractcomponents = new ArrayList<>();
    }

    public atem_WhenExistsCase(
        ArrayList<atem_AbstractComponent> atem_abstractcomponents    ) {
        this.atem_abstractcomponents = atem_abstractcomponents;
    }


    public atem_Definition getAtem_definition() {
        return atem_definition;
    }

    public void setAtem_definition(atem_Definition atem_definition) {
        this.atem_definition = atem_definition;
    }
    public List<atem_AbstractComponent> getAtem_abstractcomponents() {
        return atem_abstractcomponents;
    }

    public void addAtem_abstractcomponent(Atem_abstractcomponent atem_abstractcomponent) {
        this.atem_abstractcomponents.add(atem_abstractcomponent);
    }
    public atem_WhenExists getAtem_whenexists() {
        return atem_whenexists;
    }

    public void setAtem_whenexists(atem_WhenExists atem_whenexists) {
        this.atem_whenexists = atem_whenexists;
    }

}