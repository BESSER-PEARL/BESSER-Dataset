





import java.util.List;
import java.util.ArrayList;

public class atem_WhenDateCase  {

    private String dsl_WhenDate_Case_Month;





    private atem_WhenSundayAfterElevationOfCrossDay atem_whensundayafterelevationofcrossday;




    private atem_WhenDate atem_whendate;




    private List<atem_AbstractComponent> atem_abstractcomponents;


    public atem_WhenDateCase(
        String dsl_WhenDate_Case_Month    ) {
        this.dsl_WhenDate_Case_Month = dsl_WhenDate_Case_Month;
        this.atem_abstractcomponents = new ArrayList<>();
    }

    public atem_WhenDateCase(
        String dsl_WhenDate_Case_Month        ArrayList<atem_AbstractComponent> atem_abstractcomponents    ) {
        this.dsl_WhenDate_Case_Month = dsl_WhenDate_Case_Month;
        this.atem_abstractcomponents = atem_abstractcomponents;
    }

    public String getDsl_whendate_case_month() {
        return dsl_WhenDate_Case_Month;
    }

    public void setDsl_whendate_case_month(String dsl_WhenDate_Case_Month) {
        this.dsl_WhenDate_Case_Month = dsl_WhenDate_Case_Month;
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
    public List<atem_AbstractComponent> getAtem_abstractcomponents() {
        return atem_abstractcomponents;
    }

    public void addAtem_abstractcomponent(Atem_abstractcomponent atem_abstractcomponent) {
        this.atem_abstractcomponents.add(atem_abstractcomponent);
    }

}