





import java.util.List;
import java.util.ArrayList;

public class model_Correlation extends BPELExtensibleElement {

    private String initiate;
    private String pattern;





    private model_CorrelationSet model_correlationset;


    public model_Correlation(
        String initiate,        String pattern    ) {
        super(
        );
        this.initiate = initiate;
        this.pattern = pattern;
    }


    public String getInitiate() {
        return initiate;
    }

    public void setInitiate(String initiate) {
        this.initiate = initiate;
    }
    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }

    public model_CorrelationSet getModel_correlationset() {
        return model_correlationset;
    }

    public void setModel_correlationset(model_CorrelationSet model_correlationset) {
        this.model_correlationset = model_correlationset;
    }

}