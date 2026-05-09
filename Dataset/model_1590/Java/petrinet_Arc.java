





import java.util.List;
import java.util.ArrayList;

public class petrinet_Arc  {

    private String w;





    private petrinet_PNGraph petrinet_pngraph;


    public petrinet_Arc(
        String w    ) {
        this.w = w;
    }


    public String getW() {
        return w;
    }

    public void setW(String w) {
        this.w = w;
    }

    public petrinet_PNGraph getPetrinet_pngraph() {
        return petrinet_pngraph;
    }

    public void setPetrinet_pngraph(petrinet_PNGraph petrinet_pngraph) {
        this.petrinet_pngraph = petrinet_pngraph;
    }

}