





import java.util.List;
import java.util.ArrayList;

public class model_Correlations extends BPELExtensibleElement {






    private model_OnMessage model_onmessage;




    private List<model_Correlation> model_correlations;




    private model_OnEvent model_onevent;


    public model_Correlations(
    ) {
        super(
        );
        this.model_correlations = new ArrayList<>();
    }

    public model_Correlations(
        ArrayList<model_Correlation> model_correlations    ) {
        this.model_correlations = model_correlations;
    }


    public model_OnMessage getModel_onmessage() {
        return model_onmessage;
    }

    public void setModel_onmessage(model_OnMessage model_onmessage) {
        this.model_onmessage = model_onmessage;
    }
    public List<model_Correlation> getModel_correlations() {
        return model_correlations;
    }

    public void addModel_correlation(Model_correlation model_correlation) {
        this.model_correlations.add(model_correlation);
    }
    public model_OnEvent getModel_onevent() {
        return model_onevent;
    }

    public void setModel_onevent(model_OnEvent model_onevent) {
        this.model_onevent = model_onevent;
    }

}