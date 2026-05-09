





import java.util.List;
import java.util.ArrayList;

public class atem_AtemModel  {

    private String name;





    private List<atem_AbstractComponent> atem_abstractcomponents;


    public atem_AtemModel(
        String name    ) {
        this.name = name;
        this.atem_abstractcomponents = new ArrayList<>();
    }

    public atem_AtemModel(
        String name        ArrayList<atem_AbstractComponent> atem_abstractcomponents    ) {
        this.name = name;
        this.atem_abstractcomponents = atem_abstractcomponents;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<atem_AbstractComponent> getAtem_abstractcomponents() {
        return atem_abstractcomponents;
    }

    public void addAtem_abstractcomponent(Atem_abstractcomponent atem_abstractcomponent) {
        this.atem_abstractcomponents.add(atem_abstractcomponent);
    }

}