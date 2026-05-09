





import java.util.List;
import java.util.ArrayList;

public class stateChart_Transition  {

    private String metadata;
    private String name;
    private String TE;



    public stateChart_Transition(
        String metadata,        String name,        String TE    ) {
        this.metadata = metadata;
        this.name = name;
        this.TE = TE;
    }


    public String getMetadata() {
        return metadata;
    }

    public void setMetadata(String metadata) {
        this.metadata = metadata;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTe() {
        return TE;
    }

    public void setTe(String TE) {
        this.TE = TE;
    }


}