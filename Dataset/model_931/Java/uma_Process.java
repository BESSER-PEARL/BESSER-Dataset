





import java.util.List;
import java.util.ArrayList;

public class uma_Process extends Activity {






    private uma_ProcessComponent uma_processcomponent;




    private uma_MethodConfiguration uma_methodconfiguration;




    private List<uma_MethodConfiguration> uma_methodconfigurations;


    public uma_Process(
    ) {
        super(
        );
        this.uma_methodconfigurations = new ArrayList<>();
    }

    public uma_Process(
        ArrayList<uma_MethodConfiguration> uma_methodconfigurations    ) {
        this.uma_methodconfigurations = uma_methodconfigurations;
    }


    public uma_ProcessComponent getUma_processcomponent() {
        return uma_processcomponent;
    }

    public void setUma_processcomponent(uma_ProcessComponent uma_processcomponent) {
        this.uma_processcomponent = uma_processcomponent;
    }
    public uma_MethodConfiguration getUma_methodconfiguration() {
        return uma_methodconfiguration;
    }

    public void setUma_methodconfiguration(uma_MethodConfiguration uma_methodconfiguration) {
        this.uma_methodconfiguration = uma_methodconfiguration;
    }
    public List<uma_MethodConfiguration> getUma_methodconfigurations() {
        return uma_methodconfigurations;
    }

    public void addUma_methodconfiguration(Uma_methodconfiguration uma_methodconfiguration) {
        this.uma_methodconfigurations.add(uma_methodconfiguration);
    }

}