





import java.util.List;
import java.util.ArrayList;

public class vml_StackBars extends ChartElement {






    private vml_StackBarChart vml_stackbarchart;




    private List<vml_Bar> vml_bars;


    public vml_StackBars(
    ) {
        super(
        );
        this.vml_bars = new ArrayList<>();
    }

    public vml_StackBars(
        ArrayList<vml_Bar> vml_bars    ) {
        this.vml_bars = vml_bars;
    }


    public vml_StackBarChart getVml_stackbarchart() {
        return vml_stackbarchart;
    }

    public void setVml_stackbarchart(vml_StackBarChart vml_stackbarchart) {
        this.vml_stackbarchart = vml_stackbarchart;
    }
    public List<vml_Bar> getVml_bars() {
        return vml_bars;
    }

    public void addVml_bar(Vml_bar vml_bar) {
        this.vml_bars.add(vml_bar);
    }

}