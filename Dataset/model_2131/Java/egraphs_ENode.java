





import java.util.List;
import java.util.ArrayList;

public class egraphs_ENode  {

    private String element;





    private egraphs_EGraph egraphs_egraph;


    public egraphs_ENode(
        String element    ) {
        this.element = element;
    }


    public String getElement() {
        return element;
    }

    public void setElement(String element) {
        this.element = element;
    }

    public egraphs_EGraph getEgraphs_egraph() {
        return egraphs_egraph;
    }

    public void setEgraphs_egraph(egraphs_EGraph egraphs_egraph) {
        this.egraphs_egraph = egraphs_egraph;
    }

}