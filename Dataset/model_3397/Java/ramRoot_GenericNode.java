





import java.util.List;
import java.util.ArrayList;

public class ramRoot_GenericNode extends MT__Element {






    private List<ramRoot_MT__Element> ramroot_mt__elements;


    public ramRoot_GenericNode(
    ) {
        super(
        );
        this.ramroot_mt__elements = new ArrayList<>();
    }

    public ramRoot_GenericNode(
        ArrayList<ramRoot_MT__Element> ramroot_mt__elements    ) {
        this.ramroot_mt__elements = ramroot_mt__elements;
    }


    public List<ramRoot_MT__Element> getRamroot_mt__elements() {
        return ramroot_mt__elements;
    }

    public void addRamroot_mt__element(Ramroot_mt__element ramroot_mt__element) {
        this.ramroot_mt__elements.add(ramroot_mt__element);
    }

}