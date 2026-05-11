





import java.util.List;
import java.util.ArrayList;

public class jpdl31_Goal  {

    private String description;
    private String id;





    private jpdl31_ExperimentalPlan jpdl31_experimentalplan;




    private jpdl31_Hyphotesis jpdl31_hyphotesis;




    private List<jpdl31_Hyphotesis> jpdl31_hyphotesiss;


    public jpdl31_Goal(
        String description,        String id    ) {
        this.description = description;
        this.id = id;
        this.jpdl31_hyphotesiss = new ArrayList<>();
    }

    public jpdl31_Goal(
        String description,        String id        ArrayList<jpdl31_Hyphotesis> jpdl31_hyphotesiss    ) {
        this.description = description;
        this.id = id;
        this.jpdl31_hyphotesiss = jpdl31_hyphotesiss;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public jpdl31_ExperimentalPlan getJpdl31_experimentalplan() {
        return jpdl31_experimentalplan;
    }

    public void setJpdl31_experimentalplan(jpdl31_ExperimentalPlan jpdl31_experimentalplan) {
        this.jpdl31_experimentalplan = jpdl31_experimentalplan;
    }
    public jpdl31_Hyphotesis getJpdl31_hyphotesis() {
        return jpdl31_hyphotesis;
    }

    public void setJpdl31_hyphotesis(jpdl31_Hyphotesis jpdl31_hyphotesis) {
        this.jpdl31_hyphotesis = jpdl31_hyphotesis;
    }
    public List<jpdl31_Hyphotesis> getJpdl31_hyphotesiss() {
        return jpdl31_hyphotesiss;
    }

    public void addJpdl31_hyphotesis(Jpdl31_hyphotesis jpdl31_hyphotesis) {
        this.jpdl31_hyphotesiss.add(jpdl31_hyphotesis);
    }

}