





import java.util.List;
import java.util.ArrayList;

public class vhdl_configuration_Configuration extends Named, Module {






    private BlockConfiguration blockconfiguration;


    public vhdl_configuration_Configuration(
    ) {
        super(
        );
    }



    public BlockConfiguration getBlockconfiguration() {
        return blockconfiguration;
    }

    public void setBlockconfiguration(BlockConfiguration blockconfiguration) {
        this.blockconfiguration = blockconfiguration;
    }

}