





import java.util.List;
import java.util.ArrayList;

public class jpdl31_Level  {

    private String name;





    private jpdl31_Subhypotheses jpdl31_subhypotheses;




    private jpdl31_Hyphotesis jpdl31_hyphotesis;


    public jpdl31_Level(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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