





import java.util.List;
import java.util.ArrayList;

public class ram_InteractionFragment  {






    private ram_Lifeline ram_lifeline;




    private List<ram_Lifeline> ram_lifelines;


    public ram_InteractionFragment(
    ) {
        this.ram_lifelines = new ArrayList<>();
    }

    public ram_InteractionFragment(
        ArrayList<ram_Lifeline> ram_lifelines    ) {
        this.ram_lifelines = ram_lifelines;
    }


    public ram_Lifeline getRam_lifeline() {
        return ram_lifeline;
    }

    public void setRam_lifeline(ram_Lifeline ram_lifeline) {
        this.ram_lifeline = ram_lifeline;
    }
    public List<ram_Lifeline> getRam_lifelines() {
        return ram_lifelines;
    }

    public void addRam_lifeline(Ram_lifeline ram_lifeline) {
        this.ram_lifelines.add(ram_lifeline);
    }

}