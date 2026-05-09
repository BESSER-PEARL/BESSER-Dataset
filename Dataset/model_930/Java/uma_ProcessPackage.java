





import java.util.List;
import java.util.ArrayList;

public class uma_ProcessPackage extends MethodPackage {






    private List<uma_ProcessElement> uma_processelements;


    public uma_ProcessPackage(
    ) {
        super(
        );
        this.uma_processelements = new ArrayList<>();
    }

    public uma_ProcessPackage(
        ArrayList<uma_ProcessElement> uma_processelements    ) {
        this.uma_processelements = uma_processelements;
    }


    public List<uma_ProcessElement> getUma_processelements() {
        return uma_processelements;
    }

    public void addUma_processelement(Uma_processelement uma_processelement) {
        this.uma_processelements.add(uma_processelement);
    }

}