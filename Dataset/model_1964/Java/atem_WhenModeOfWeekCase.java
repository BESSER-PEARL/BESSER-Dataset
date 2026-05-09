





import java.util.List;
import java.util.ArrayList;

public class atem_WhenModeOfWeekCase  {






    private atem_ModeOfWeekSet atem_modeofweekset;




    private atem_WhenModeOfWeek atem_whenmodeofweek;




    private List<atem_AbstractComponent> atem_abstractcomponents;


    public atem_WhenModeOfWeekCase(
    ) {
        this.atem_abstractcomponents = new ArrayList<>();
    }

    public atem_WhenModeOfWeekCase(
        ArrayList<atem_AbstractComponent> atem_abstractcomponents    ) {
        this.atem_abstractcomponents = atem_abstractcomponents;
    }


    public atem_ModeOfWeekSet getAtem_modeofweekset() {
        return atem_modeofweekset;
    }

    public void setAtem_modeofweekset(atem_ModeOfWeekSet atem_modeofweekset) {
        this.atem_modeofweekset = atem_modeofweekset;
    }
    public atem_WhenModeOfWeek getAtem_whenmodeofweek() {
        return atem_whenmodeofweek;
    }

    public void setAtem_whenmodeofweek(atem_WhenModeOfWeek atem_whenmodeofweek) {
        this.atem_whenmodeofweek = atem_whenmodeofweek;
    }
    public List<atem_AbstractComponent> getAtem_abstractcomponents() {
        return atem_abstractcomponents;
    }

    public void addAtem_abstractcomponent(Atem_abstractcomponent atem_abstractcomponent) {
        this.atem_abstractcomponents.add(atem_abstractcomponent);
    }

}