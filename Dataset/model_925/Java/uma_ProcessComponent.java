





import java.util.List;
import java.util.ArrayList;

public class uma_ProcessComponent extends MethodUnit, ProcessPackage {






    private uma_ProcessComponentDescriptor uma_processcomponentdescriptor;




    private uma_Process uma_process;




    private List<uma_ProcessComponentInterface> uma_processcomponentinterfaces;


    public uma_ProcessComponent(
    ) {
        super(
        );
        this.uma_processcomponentinterfaces = new ArrayList<>();
    }

    public uma_ProcessComponent(
        ArrayList<uma_ProcessComponentInterface> uma_processcomponentinterfaces    ) {
        this.uma_processcomponentinterfaces = uma_processcomponentinterfaces;
    }


    public uma_ProcessComponentDescriptor getUma_processcomponentdescriptor() {
        return uma_processcomponentdescriptor;
    }

    public void setUma_processcomponentdescriptor(uma_ProcessComponentDescriptor uma_processcomponentdescriptor) {
        this.uma_processcomponentdescriptor = uma_processcomponentdescriptor;
    }
    public uma_Process getUma_process() {
        return uma_process;
    }

    public void setUma_process(uma_Process uma_process) {
        this.uma_process = uma_process;
    }
    public List<uma_ProcessComponentInterface> getUma_processcomponentinterfaces() {
        return uma_processcomponentinterfaces;
    }

    public void addUma_processcomponentinterface(Uma_processcomponentinterface uma_processcomponentinterface) {
        this.uma_processcomponentinterfaces.add(uma_processcomponentinterface);
    }

}