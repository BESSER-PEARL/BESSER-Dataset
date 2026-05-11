





import java.util.List;
import java.util.ArrayList;

public class builds_TestElement  {

    private String duration;
    private String output;
    private String label;
    private String errorOutput;



    public builds_TestElement(
        String duration,        String output,        String label,        String errorOutput    ) {
        this.duration = duration;
        this.output = output;
        this.label = label;
        this.errorOutput = errorOutput;
    }


    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }
    public String getOutput() {
        return output;
    }

    public void setOutput(String output) {
        this.output = output;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getErroroutput() {
        return errorOutput;
    }

    public void setErroroutput(String errorOutput) {
        this.errorOutput = errorOutput;
    }


}