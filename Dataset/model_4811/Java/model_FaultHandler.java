





import java.util.List;
import java.util.ArrayList;

public class model_FaultHandler extends BPELExtensibleElement {






    private model_Process model_process;




    private model_CatchAll model_catchall;


    public model_FaultHandler(
    ) {
        super(
        );
    }



    public model_Process getModel_process() {
        return model_process;
    }

    public void setModel_process(model_Process model_process) {
        this.model_process = model_process;
    }
    public model_CatchAll getModel_catchall() {
        return model_catchall;
    }

    public void setModel_catchall(model_CatchAll model_catchall) {
        this.model_catchall = model_catchall;
    }

}