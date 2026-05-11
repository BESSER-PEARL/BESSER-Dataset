





import java.util.List;
import java.util.ArrayList;

public class llp_Task  {

    private String name;





    private llp_LowLevelProgram llp_lowlevelprogram;


    public llp_Task(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public llp_LowLevelProgram getLlp_lowlevelprogram() {
        return llp_lowlevelprogram;
    }

    public void setLlp_lowlevelprogram(llp_LowLevelProgram llp_lowlevelprogram) {
        this.llp_lowlevelprogram = llp_lowlevelprogram;
    }

}