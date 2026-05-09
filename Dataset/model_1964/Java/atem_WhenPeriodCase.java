





import java.util.List;
import java.util.ArrayList;

public class atem_WhenPeriodCase  {






    private List<atem_AbstractComponent> atem_abstractcomponents;




    private atem_WhenPentecostarionDay atem_whenpentecostarionday;




    private atem_WhenLukanCycleDay atem_whenlukancycleday;




    private atem_WhenTriodionDay atem_whentriodionday;




    private atem_WhenMovableCycleDay atem_whenmovablecycleday;


    public atem_WhenPeriodCase(
    ) {
        this.atem_abstractcomponents = new ArrayList<>();
    }

    public atem_WhenPeriodCase(
        ArrayList<atem_AbstractComponent> atem_abstractcomponents    ) {
        this.atem_abstractcomponents = atem_abstractcomponents;
    }


    public List<atem_AbstractComponent> getAtem_abstractcomponents() {
        return atem_abstractcomponents;
    }

    public void addAtem_abstractcomponent(Atem_abstractcomponent atem_abstractcomponent) {
        this.atem_abstractcomponents.add(atem_abstractcomponent);
    }
    public atem_WhenPentecostarionDay getAtem_whenpentecostarionday() {
        return atem_whenpentecostarionday;
    }

    public void setAtem_whenpentecostarionday(atem_WhenPentecostarionDay atem_whenpentecostarionday) {
        this.atem_whenpentecostarionday = atem_whenpentecostarionday;
    }
    public atem_WhenLukanCycleDay getAtem_whenlukancycleday() {
        return atem_whenlukancycleday;
    }

    public void setAtem_whenlukancycleday(atem_WhenLukanCycleDay atem_whenlukancycleday) {
        this.atem_whenlukancycleday = atem_whenlukancycleday;
    }
    public atem_WhenTriodionDay getAtem_whentriodionday() {
        return atem_whentriodionday;
    }

    public void setAtem_whentriodionday(atem_WhenTriodionDay atem_whentriodionday) {
        this.atem_whentriodionday = atem_whentriodionday;
    }
    public atem_WhenMovableCycleDay getAtem_whenmovablecycleday() {
        return atem_whenmovablecycleday;
    }

    public void setAtem_whenmovablecycleday(atem_WhenMovableCycleDay atem_whenmovablecycleday) {
        this.atem_whenmovablecycleday = atem_whenmovablecycleday;
    }

}