





import java.util.List;
import java.util.ArrayList;

public class War_TwoPlayerPointPile1  {

    private boolean inWar1;
    private String logger;
    private boolean inWar;
    private String logger1;



    public War_TwoPlayerPointPile1(
        boolean inWar1,        String logger,        boolean inWar,        String logger1    ) {
        this.inWar1 = inWar1;
        this.logger = logger;
        this.inWar = inWar;
        this.logger1 = logger1;
    }


    public boolean getInwar1() {
        return inWar1;
    }

    public void setInwar1(boolean inWar1) {
        this.inWar1 = inWar1;
    }
    public String getLogger() {
        return logger;
    }

    public void setLogger(String logger) {
        this.logger = logger;
    }
    public boolean getInwar() {
        return inWar;
    }

    public void setInwar(boolean inWar) {
        this.inWar = inWar;
    }
    public String getLogger1() {
        return logger1;
    }

    public void setLogger1(String logger1) {
        this.logger1 = logger1;
    }


}