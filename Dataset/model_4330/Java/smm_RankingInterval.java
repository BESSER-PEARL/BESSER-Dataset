





import java.util.List;
import java.util.ArrayList;

public class smm_RankingInterval extends SmmElement {

    private float minimumEndpoint;
    private float maximumEndpoint;
    private boolean maximumOpen;
    private boolean minimumOpen;
    private String symbol;



    public smm_RankingInterval(
        float minimumEndpoint,        float maximumEndpoint,        boolean maximumOpen,        boolean minimumOpen,        String symbol    ) {
        super(
        );
        this.minimumEndpoint = minimumEndpoint;
        this.maximumEndpoint = maximumEndpoint;
        this.maximumOpen = maximumOpen;
        this.minimumOpen = minimumOpen;
        this.symbol = symbol;
    }


    public float getMinimumendpoint() {
        return minimumEndpoint;
    }

    public void setMinimumendpoint(float minimumEndpoint) {
        this.minimumEndpoint = minimumEndpoint;
    }
    public float getMaximumendpoint() {
        return maximumEndpoint;
    }

    public void setMaximumendpoint(float maximumEndpoint) {
        this.maximumEndpoint = maximumEndpoint;
    }
    public boolean getMaximumopen() {
        return maximumOpen;
    }

    public void setMaximumopen(boolean maximumOpen) {
        this.maximumOpen = maximumOpen;
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


}