





import java.util.List;
import java.util.ArrayList;

public class drone_Processor extends NamedElement {

    private int frequency;
    private String architecture;



    public drone_Processor(
        int frequency,        String architecture    ) {
        super(
        );
        this.frequency = frequency;
        this.architecture = architecture;
    }


    public int getFrequency() {
        return frequency;
    }

    public void setFrequency(int frequency) {
        this.frequency = frequency;
    }
    public String getArchitecture() {
        return architecture;
    }

    public void setArchitecture(String architecture) {
        this.architecture = architecture;
    }


}