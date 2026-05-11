





import java.util.List;
import java.util.ArrayList;

public class p2_IProcessingStepDescriptor  {

    private boolean required;
    private String processorId;
    private String data;



    public p2_IProcessingStepDescriptor(
        boolean required,        String processorId,        String data    ) {
        this.required = required;
        this.processorId = processorId;
        this.data = data;
    }


    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }
    public String getProcessorid() {
        return processorId;
    }

    public void setProcessorid(String processorId) {
        this.processorId = processorId;
    }
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }


}