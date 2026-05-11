





import java.util.List;
import java.util.ArrayList;

public class jpdl31_DependentVariable  {

    private String description;
    private String name;





    private List<jpdl31_Metric> jpdl31_metrics;




    private jpdl31_Subhypotheses jpdl31_subhypotheses;




    private jpdl31_Hyphotesis jpdl31_hyphotesis;


    public jpdl31_DependentVariable(
        String description,        String name    ) {
        this.description = description;
        this.name = name;
        this.jpdl31_metrics = new ArrayList<>();
    }

    public jpdl31_DependentVariable(
        String description,        String name        ArrayList<jpdl31_Metric> jpdl31_metrics    ) {
        this.description = description;
        this.name = name;
        this.jpdl31_metrics = jpdl31_metrics;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<jpdl31_Metric> getJpdl31_metrics() {
        return jpdl31_metrics;
    }

    public void addJpdl31_metric(Jpdl31_metric jpdl31_metric) {
        this.jpdl31_metrics.add(jpdl31_metric);
    }
    public jpdl31_Subhypotheses getJpdl31_subhypotheses() {
        return jpdl31_subhypotheses;
    }

    public void setJpdl31_subhypotheses(jpdl31_Subhypotheses jpdl31_subhypotheses) {
        this.jpdl31_subhypotheses = jpdl31_subhypotheses;
    }
    public jpdl31_Hyphotesis getJpdl31_hyphotesis() {
        return jpdl31_hyphotesis;
    }

    public void setJpdl31_hyphotesis(jpdl31_Hyphotesis jpdl31_hyphotesis) {
        this.jpdl31_hyphotesis = jpdl31_hyphotesis;
    }

}