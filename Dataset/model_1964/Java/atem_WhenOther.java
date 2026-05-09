





import java.util.List;
import java.util.ArrayList;

public class atem_WhenOther  {






    private atem_WhenExists atem_whenexists;




    private atem_WhenSundaysBeforeTriodion atem_whensundaysbeforetriodion;




    private atem_WhenModeOfWeek atem_whenmodeofweek;




    private atem_WhenLukanCycleDay atem_whenlukancycleday;




    private atem_WhenDayName atem_whendayname;




    private atem_WhenSundayAfterElevationOfCrossDay atem_whensundayafterelevationofcrossday;




    private atem_WhenDate atem_whendate;




    private atem_WhenMovableCycleDay atem_whenmovablecycleday;




    private atem_WhenTriodionDay atem_whentriodionday;




    private atem_WhenPentecostarionDay atem_whenpentecostarionday;




    private List<atem_AbstractComponent> atem_abstractcomponents;


    public atem_WhenOther(
    ) {
        this.atem_abstractcomponents = new ArrayList<>();
    }

    public atem_WhenOther(
        ArrayList<atem_AbstractComponent> atem_abstractcomponents    ) {
        this.atem_abstractcomponents = atem_abstractcomponents;
    }


    public atem_WhenExists getAtem_whenexists() {
        return atem_whenexists;
    }

    public void setAtem_whenexists(atem_WhenExists atem_whenexists) {
        this.atem_whenexists = atem_whenexists;
    }
    public atem_WhenSundaysBeforeTriodion getAtem_whensundaysbeforetriodion() {
        return atem_whensundaysbeforetriodion;
    }

    public void setAtem_whensundaysbeforetriodion(atem_WhenSundaysBeforeTriodion atem_whensundaysbeforetriodion) {
        this.atem_whensundaysbeforetriodion = atem_whensundaysbeforetriodion;
    }
    public atem_WhenModeOfWeek getAtem_whenmodeofweek() {
        return atem_whenmodeofweek;
    }

    public void setAtem_whenmodeofweek(atem_WhenModeOfWeek atem_whenmodeofweek) {
        this.atem_whenmodeofweek = atem_whenmodeofweek;
    }
    public atem_WhenLukanCycleDay getAtem_whenlukancycleday() {
        return atem_whenlukancycleday;
    }

    public void setAtem_whenlukancycleday(atem_WhenLukanCycleDay atem_whenlukancycleday) {
        this.atem_whenlukancycleday = atem_whenlukancycleday;
    }
    public atem_WhenDayName getAtem_whendayname() {
        return atem_whendayname;
    }

    public void setAtem_whendayname(atem_WhenDayName atem_whendayname) {
        this.atem_whendayname = atem_whendayname;
    }
    public atem_WhenSundayAfterElevationOfCrossDay getAtem_whensundayafterelevationofcrossday() {
        return atem_whensundayafterelevationofcrossday;
    }

    public void setAtem_whensundayafterelevationofcrossday(atem_WhenSundayAfterElevationOfCrossDay atem_whensundayafterelevationofcrossday) {
        this.atem_whensundayafterelevationofcrossday = atem_whensundayafterelevationofcrossday;
    }
    public atem_WhenDate getAtem_whendate() {
        return atem_whendate;
    }

    public void setAtem_whendate(atem_WhenDate atem_whendate) {
        this.atem_whendate = atem_whendate;
    }
    public atem_WhenMovableCycleDay getAtem_whenmovablecycleday() {
        return atem_whenmovablecycleday;
    }

    public void setAtem_whenmovablecycleday(atem_WhenMovableCycleDay atem_whenmovablecycleday) {
        this.atem_whenmovablecycleday = atem_whenmovablecycleday;
    }
    public atem_WhenTriodionDay getAtem_whentriodionday() {
        return atem_whentriodionday;
    }

    public void setAtem_whentriodionday(atem_WhenTriodionDay atem_whentriodionday) {
        this.atem_whentriodionday = atem_whentriodionday;
    }
    public atem_WhenPentecostarionDay getAtem_whenpentecostarionday() {
        return atem_whenpentecostarionday;
    }

    public void setAtem_whenpentecostarionday(atem_WhenPentecostarionDay atem_whenpentecostarionday) {
        this.atem_whenpentecostarionday = atem_whenpentecostarionday;
    }
    public List<atem_AbstractComponent> getAtem_abstractcomponents() {
        return atem_abstractcomponents;
    }

    public void addAtem_abstractcomponent(Atem_abstractcomponent atem_abstractcomponent) {
        this.atem_abstractcomponents.add(atem_abstractcomponent);
    }

}