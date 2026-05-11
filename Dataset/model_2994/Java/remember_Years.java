





import java.util.List;
import java.util.ArrayList;

public class remember_Years  {






    private List<remember_Year> remember_years;




    private remember_Year remember_year;


    public remember_Years(
    ) {
        this.remember_years = new ArrayList<>();
    }

    public remember_Years(
        ArrayList<remember_Year> remember_years    ) {
        this.remember_years = remember_years;
    }


    public List<remember_Year> getRemember_years() {
        return remember_years;
    }

    public void addRemember_year(Remember_year remember_year) {
        this.remember_years.add(remember_year);
    }
    public remember_Year getRemember_year() {
        return remember_year;
    }

    public void setRemember_year(remember_Year remember_year) {
        this.remember_year = remember_year;
    }

}