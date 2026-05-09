





import java.util.List;
import java.util.ArrayList;

public class devs_OutputEvent extends Event {






    private List<devs_OutputFunction> devs_outputfunctions;




    private devs_OutputFunction devs_outputfunction;


    public devs_OutputEvent(
    ) {
        super(
        );
        this.devs_outputfunctions = new ArrayList<>();
    }

    public devs_OutputEvent(
        ArrayList<devs_OutputFunction> devs_outputfunctions    ) {
        this.devs_outputfunctions = devs_outputfunctions;
    }


    public List<devs_OutputFunction> getDevs_outputfunctions() {
        return devs_outputfunctions;
    }

    public void addDevs_outputfunction(Devs_outputfunction devs_outputfunction) {
        this.devs_outputfunctions.add(devs_outputfunction);
    }
    public devs_OutputFunction getDevs_outputfunction() {
        return devs_outputfunction;
    }

    public void setDevs_outputfunction(devs_OutputFunction devs_outputfunction) {
        this.devs_outputfunction = devs_outputfunction;
    }

}