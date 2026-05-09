





import java.util.List;
import java.util.ArrayList;

public class library_GuideBookWriter extends Writer {

    private String countries;



    public library_GuideBookWriter(
        String countries    ) {
        super(
        );
        this.countries = countries;
    }


    public String getCountries() {
        return countries;
    }

    public void setCountries(String countries) {
        this.countries = countries;
    }


}