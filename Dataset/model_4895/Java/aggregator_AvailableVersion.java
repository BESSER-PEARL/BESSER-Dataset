





import java.util.List;
import java.util.ArrayList;

public class aggregator_AvailableVersion  {

    private String availableFrom;
    private String filter;
    private String version;
    private String versionMatch;





    private aggregator_AvailableVersionsHeader aggregator_availableversionsheader;




    private aggregator_InstallableUnitRequest aggregator_installableunitrequest;


    public aggregator_AvailableVersion(
        String availableFrom,        String filter,        String version,        String versionMatch    ) {
        this.availableFrom = availableFrom;
        this.filter = filter;
        this.version = version;
        this.versionMatch = versionMatch;
    }


    public String getAvailablefrom() {
        return availableFrom;
    }

    public void setAvailablefrom(String availableFrom) {
        this.availableFrom = availableFrom;
    }
    public String getFilter() {
        return filter;
    }

    public void setFilter(String filter) {
        this.filter = filter;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getVersionmatch() {
        return versionMatch;
    }

    public void setVersionmatch(String versionMatch) {
        this.versionMatch = versionMatch;
    }

    public aggregator_AvailableVersionsHeader getAggregator_availableversionsheader() {
        return aggregator_availableversionsheader;
    }

    public void setAggregator_availableversionsheader(aggregator_AvailableVersionsHeader aggregator_availableversionsheader) {
        this.aggregator_availableversionsheader = aggregator_availableversionsheader;
    }
    public aggregator_InstallableUnitRequest getAggregator_installableunitrequest() {
        return aggregator_installableunitrequest;
    }

    public void setAggregator_installableunitrequest(aggregator_InstallableUnitRequest aggregator_installableunitrequest) {
        this.aggregator_installableunitrequest = aggregator_installableunitrequest;
    }

}