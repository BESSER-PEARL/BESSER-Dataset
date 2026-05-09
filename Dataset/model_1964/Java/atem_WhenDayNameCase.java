





import java.util.List;
import java.util.ArrayList;

public class atem_WhenDayNameCase  {






    private atem_WhenDayName atem_whendayname;




    private List<atem_AbstractComponent> atem_abstractcomponents;


    public atem_WhenDayNameCase(
    ) {
        this.atem_abstractcomponents = new ArrayList<>();
    }

    public atem_WhenDayNameCase(
        ArrayList<atem_AbstractComponent> atem_abstractcomponents    ) {
        this.atem_abstractcomponents = atem_abstractcomponents;
    }


    public atem_WhenDayName getAtem_whendayname() {
        return atem_whendayname;
    }

    public void setAtem_whendayname(atem_WhenDayName atem_whendayname) {
        this.atem_whendayname = atem_whendayname;
    }
    public List<atem_AbstractComponent> getAtem_abstractcomponents() {
        return atem_abstractcomponents;
    }

    public void addAtem_abstractcomponent(Atem_abstractcomponent atem_abstractcomponent) {
        this.atem_abstractcomponents.add(atem_abstractcomponent);
    }

}