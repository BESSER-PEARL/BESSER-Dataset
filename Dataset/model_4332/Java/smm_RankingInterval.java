





import java.util.List;
import java.util.ArrayList;

public class smm_RankingInterval extends SmmElement {

    private String symbol;
    private boolean minimumOpen;
    private float minimumEndpoint;
    private boolean maximumOpen;
    private float maximumEndpoint;



    public smm_RankingInterval(
        String symbol,        boolean minimumOpen,        float minimumEndpoint,        boolean maximumOpen,        float maximumEndpoint    ) {
        super(
        );
        this.symbol = symbol;
        this.minimumOpen = minimumOpen;
        this.minimumEndpoint = minimumEndpoint;
        this.maximumOpen = maximumOpen;
        this.maximumEndpoint = maximumEndpoint;
    }


    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }
    public boolean getMinimumopen() {
        return minimumOpen;
    }

    public void setMinimumopen(boolean minimumOpen) {
        this.minimumOpen = minimumOpen;
    }
    public float getMinimumendpoint() {
        return minimumEndpoint;
    }

    public void setMinimumendpoint(float minimumEndpoint) {
        this.minimumEndpoint = minimumEndpoint;
    }
    public boolean getMaximumopen() {
        return maximumOpen;
    }

    public void setMaximumopen(boolean maximumOpen) {
        this.maximumOpen = maximumOpen;
    }
    public float getMaximumendpoint() {
        return maximumEndpoint;
    }

    public void setMaximumendpoint(float maximumEndpoint) {
        this.maximumEndpoint = maximumEndpoint;
    }


}