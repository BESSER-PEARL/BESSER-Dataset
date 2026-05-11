





import java.util.List;
import java.util.ArrayList;

public class smm_RankingInterval extends SmmElement {

    private boolean maximumOpen;
    private float minimumEndpoint;
    private boolean minimumOpen;
    private String symbol;
    private float maximumEndpoint;



    public smm_RankingInterval(
        boolean maximumOpen,        float minimumEndpoint,        boolean minimumOpen,        String symbol,        float maximumEndpoint    ) {
        super(
        );
        this.maximumOpen = maximumOpen;
        this.minimumEndpoint = minimumEndpoint;
        this.minimumOpen = minimumOpen;
        this.symbol = symbol;
        this.maximumEndpoint = maximumEndpoint;
    }


    public boolean getMaximumopen() {
        return maximumOpen;
    }

    public void setMaximumopen(boolean maximumOpen) {
        this.maximumOpen = maximumOpen;
    }
    public float getMinimumendpoint() {
        return minimumEndpoint;
    }

    public void setMinimumendpoint(float minimumEndpoint) {
        this.minimumEndpoint = minimumEndpoint;
    }
    public boolean getMinimumopen() {
        return minimumOpen;
    }

    public void setMinimumopen(boolean minimumOpen) {
        this.minimumOpen = minimumOpen;
    }
    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }
    public float getMaximumendpoint() {
        return maximumEndpoint;
    }

    public void setMaximumendpoint(float maximumEndpoint) {
        this.maximumEndpoint = maximumEndpoint;
    }


}