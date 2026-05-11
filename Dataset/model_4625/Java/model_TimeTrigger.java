





import java.util.List;
import java.util.ArrayList;

public class model_TimeTrigger  {

    private String period;
    private String onTrigger;





    private model_Symbol model_symbol;


    public model_TimeTrigger(
        String period,        String onTrigger    ) {
        this.period = period;
        this.onTrigger = onTrigger;
    }


    public String getPeriod() {
        return period;
    }

    public void setPeriod(String period) {
        this.period = period;
    }
    public String getOntrigger() {
        return onTrigger;
    }

    public void setOntrigger(String onTrigger) {
        this.onTrigger = onTrigger;
    }

    public model_Symbol getModel_symbol() {
        return model_symbol;
    }

    public void setModel_symbol(model_Symbol model_symbol) {
        this.model_symbol = model_symbol;
    }

}