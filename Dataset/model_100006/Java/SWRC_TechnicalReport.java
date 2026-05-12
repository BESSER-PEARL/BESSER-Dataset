





import java.util.List;
import java.util.ArrayList;

public class SWRC_TechnicalReport extends Report {

    private String series;





    private Organization organization;


    public SWRC_TechnicalReport(
        String series    ) {
        super(
        );
        this.series = series;
    }


    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
        this.series = series;
    }

    public Organization getOrganization() {
        return organization;
    }

    public void setOrganization(Organization organization) {
        this.organization = organization;
    }

}