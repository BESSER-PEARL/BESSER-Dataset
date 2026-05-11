





import java.util.List;
import java.util.ArrayList;

public class fsa_State  {

    private String name;
    private boolean final;
    private String temporalProperties;



    public fsa_State(
        String name,        boolean final,        String temporalProperties    ) {
        this.name = name;
        this.final = final;
        this.temporalProperties = temporalProperties;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }
    public String getTemporalproperties() {
        return temporalProperties;
    }

    public void setTemporalproperties(String temporalProperties) {
        this.temporalProperties = temporalProperties;
    }


}