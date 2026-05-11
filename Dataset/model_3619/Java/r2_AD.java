





import java.util.List;
import java.util.ArrayList;

public class r2_AD extends ANY {

    private String use;





    private List<r2_ADXP> r2_adxps;


    public r2_AD(
        String use    ) {
        super(
        );
        this.use = use;
        this.r2_adxps = new ArrayList<>();
    }

    public r2_AD(
        String use        ArrayList<r2_ADXP> r2_adxps    ) {
        this.use = use;
        this.r2_adxps = r2_adxps;
    }

    public String getUse() {
        return use;
    }

    public void setUse(String use) {
        this.use = use;
    }

    public List<r2_ADXP> getR2_adxps() {
        return r2_adxps;
    }

    public void addR2_adxp(R2_adxp r2_adxp) {
        this.r2_adxps.add(r2_adxp);
    }

}