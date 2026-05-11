





import java.util.List;
import java.util.ArrayList;

public class xpdl2_extensions_LoopDataRefType  {

    private String inputItemRef;
    private String outputItemRef;
    private String loopCounterRef;



    public xpdl2_extensions_LoopDataRefType(
        String inputItemRef,        String outputItemRef,        String loopCounterRef    ) {
        this.inputItemRef = inputItemRef;
        this.outputItemRef = outputItemRef;
        this.loopCounterRef = loopCounterRef;
    }


    public String getInputitemref() {
        return inputItemRef;
    }

    public void setInputitemref(String inputItemRef) {
        this.inputItemRef = inputItemRef;
    }
    public String getOutputitemref() {
        return outputItemRef;
    }

    public void setOutputitemref(String outputItemRef) {
        this.outputItemRef = outputItemRef;
    }
    public String getLoopcounterref() {
        return loopCounterRef;
    }

    public void setLoopcounterref(String loopCounterRef) {
        this.loopCounterRef = loopCounterRef;
    }


}