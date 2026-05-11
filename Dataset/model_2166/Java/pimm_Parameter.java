





import java.util.List;
import java.util.ArrayList;

public class pimm_Parameter extends AbstractVertex, ISetter {

    private boolean configurationInterface;



    public pimm_Parameter(
        boolean configurationInterface    ) {
        super(
        );
        this.configurationInterface = configurationInterface;
    }


    public boolean getConfigurationinterface() {
        return configurationInterface;
    }

    public void setConfigurationinterface(boolean configurationInterface) {
        this.configurationInterface = configurationInterface;
    }


}