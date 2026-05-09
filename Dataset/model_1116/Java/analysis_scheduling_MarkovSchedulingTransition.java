





import java.util.List;
import java.util.ArrayList;

public class analysis_scheduling_MarkovSchedulingTransition  {

    private String name;
    private String firings;



    public analysis_scheduling_MarkovSchedulingTransition(
        String name,        String firings    ) {
        this.name = name;
        this.firings = firings;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFirings() {
        return firings;
    }

    public void setFirings(String firings) {
        this.firings = firings;
    }


}