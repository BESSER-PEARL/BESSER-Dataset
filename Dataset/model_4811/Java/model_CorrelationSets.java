





import java.util.List;
import java.util.ArrayList;

public class model_CorrelationSets extends BPELExtensibleElement {






    private List<model_CorrelationSet> model_correlationsets;




    private model_Process model_process;




    private model_OnEvent model_onevent;


    public model_CorrelationSets(
    ) {
        super(
        );
        this.model_correlationsets = new ArrayList<>();
    }

    public model_CorrelationSets(
        ArrayList<model_CorrelationSet> model_correlationsets    ) {
        this.model_correlationsets = model_correlationsets;
    }


    public List<model_CorrelationSet> getModel_correlationsets() {
        return model_correlationsets;
    }

    public void addModel_correlationset(Model_correlationset model_correlationset) {
        this.model_correlationsets.add(model_correlationset);
    }
    public model_Process getModel_process() {
        return model_process;
    }

    public void setModel_process(model_Process model_process) {
        this.model_process = model_process;
    }
    public model_OnEvent getModel_onevent() {
        return model_onevent;
    }

    public void setModel_onevent(model_OnEvent model_onevent) {
        this.model_onevent = model_onevent;
    }

}