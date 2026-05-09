





import java.util.List;
import java.util.ArrayList;

public class MARTE_Library_BasicNFP_Types_NFP_Duration extends NFP_Real {

    private String precision;
    private String clock;
    private String best;
    private String worst;
    private String unit;



    public MARTE_Library_BasicNFP_Types_NFP_Duration(
        String precision,        String clock,        String best,        String worst,        String unit    ) {
        super(
        );
        this.precision = precision;
        this.clock = clock;
        this.best = best;
        this.worst = worst;
        this.unit = unit;
    }


    public String getPrecision() {
        return precision;
    }

    public void setPrecision(String precision) {
        this.precision = precision;
    }
    public String getClock() {
        return clock;
    }

    public void setClock(String clock) {
        this.clock = clock;
    }
    public String getBest() {
        return best;
    }

    public void setBest(String best) {
        this.best = best;
    }
    public String getWorst() {
        return worst;
    }

    public void setWorst(String worst) {
        this.worst = worst;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }


}