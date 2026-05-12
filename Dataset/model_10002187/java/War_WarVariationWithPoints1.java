





import java.util.List;
import java.util.ArrayList;

public class War_WarVariationWithPoints1  {

    private boolean inWar1;
    private boolean inWar;
    private String logger;
    private String logger1;



    public War_WarVariationWithPoints1(
        boolean inWar1,        boolean inWar,        String logger,        String logger1    ) {
        this.inWar1 = inWar1;
        this.inWar = inWar;
        this.logger = logger;
        this.logger1 = logger1;
    }


    public boolean getInwar1() {
        return inWar1;
    }

    public void setInwar1(boolean inWar1) {
        this.inWar1 = inWar1;
    }
    public boolean getInwar() {
        return inWar;
    }

    public void setInwar(boolean inWar) {
        this.inWar = inWar;
    }
    public String getLogger() {
        return logger;
    }

    public void setLogger(String logger) {
        this.logger = logger;
    }
    public String getLogger1() {
        return logger1;
    }

    public void setLogger1(String logger1) {
        this.logger1 = logger1;
    }


}