





import java.util.List;
import java.util.ArrayList;

public class model_Ball  {

    private String runs;
    private int runValue;
    private String switchEnds;





    private model_Player model_player;




    private model_Player model_player;




    private model_Over model_over;


    public model_Ball(
        String runs,        int runValue,        String switchEnds    ) {
        this.runs = runs;
        this.runValue = runValue;
        this.switchEnds = switchEnds;
    }


    public String getRuns() {
        return runs;
    }

    public void setRuns(String runs) {
        this.runs = runs;
    }
    public int getRunvalue() {
        return runValue;
    }

    public void setRunvalue(int runValue) {
        this.runValue = runValue;
    }
    public String getSwitchends() {
        return switchEnds;
    }

    public void setSwitchends(String switchEnds) {
        this.switchEnds = switchEnds;
    }

    public model_Player getModel_player() {
        return model_player;
    }

    public void setModel_player(model_Player model_player) {
        this.model_player = model_player;
    }
    public model_Player getModel_player() {
        return model_player;
    }

    public void setModel_player(model_Player model_player) {
        this.model_player = model_player;
    }
    public model_Over getModel_over() {
        return model_over;
    }

    public void setModel_over(model_Over model_over) {
        this.model_over = model_over;
    }

}