





import java.util.List;
import java.util.ArrayList;

public class smm_RankingInterval extends SmmElement {

    private String minimumEndpoint;
    private String maximumEndpoint;
    private String symbol;
    private String minimumOpen;
    private String maximumOpen;



    public smm_RankingInterval(
        String minimumEndpoint,        String maximumEndpoint,        String symbol,        String minimumOpen,        String maximumOpen    ) {
        super(
        );
        this.minimumEndpoint = minimumEndpoint;
        this.maximumEndpoint = maximumEndpoint;
        this.symbol = symbol;
        this.minimumOpen = minimumOpen;
        this.maximumOpen = maximumOpen;
    }


    public String getMinimumendpoint() {
        return minimumEndpoint;
    }

    public void setMinimumendpoint(String minimumEndpoint) {
        this.minimumEndpoint = minimumEndpoint;
    }
    public String getMaximumendpoint() {
        return maximumEndpoint;
    }

    public void setMaximumendpoint(String maximumEndpoint) {
        this.maximumEndpoint = maximumEndpoint;
    }
    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }
    public String getMinimumopen() {
        return minimumOpen;
    }

    public void setMinimumopen(String minimumOpen) {
        this.minimumOpen = minimumOpen;
    }
    public String getMaximumopen() {
        return maximumOpen;
    }

    public void setMaximumopen(String maximumOpen) {
        this.maximumOpen = maximumOpen;
    }


}