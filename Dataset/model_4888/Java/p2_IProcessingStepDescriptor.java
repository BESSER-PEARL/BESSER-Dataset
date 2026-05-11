





import java.util.List;
import java.util.ArrayList;

public class p2_IProcessingStepDescriptor  {

    private boolean required;
    private String data;
    private String processorId;



    public p2_IProcessingStepDescriptor(
        boolean required,        String data,        String processorId    ) {
        this.required = required;
        this.data = data;
        this.processorId = processorId;
    }


    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }
    public String getProcessorid() {
        return processorId;
    }

    public void setProcessorid(String processorId) {
        this.processorId = processorId;
    }


}