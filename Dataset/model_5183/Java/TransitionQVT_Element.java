





import java.util.List;
import java.util.ArrayList;

public class TransitionQVT_Element  {

    private int id;





    private TransitionQVT_Root transitionqvt_root;




    private List<TransitionQVT_Element> transitionqvt_elements;


    public TransitionQVT_Element(
        int id    ) {
        this.id = id;
        this.transitionqvt_elements = new ArrayList<>();
    }

    public TransitionQVT_Element(
        int id        ArrayList<TransitionQVT_Element> transitionqvt_elements    ) {
        this.id = id;
        this.transitionqvt_elements = transitionqvt_elements;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public TransitionQVT_Root getTransitionqvt_root() {
        return transitionqvt_root;
    }

    public void setTransitionqvt_root(TransitionQVT_Root transitionqvt_root) {
        this.transitionqvt_root = transitionqvt_root;
    }
    public List<TransitionQVT_Element> getTransitionqvt_elements() {
        return transitionqvt_elements;
    }

    public void addTransitionqvt_element(Transitionqvt_element transitionqvt_element) {
        this.transitionqvt_elements.add(transitionqvt_element);
    }

}