





import java.util.List;
import java.util.ArrayList;

public class source_SRoot extends SElement {






    private List<source_X> source_xs;


    public source_SRoot(
    ) {
        super(
        );
        this.source_xs = new ArrayList<>();
    }

    public source_SRoot(
        ArrayList<source_X> source_xs    ) {
        this.source_xs = source_xs;
    }


    public List<source_X> getSource_xs() {
        return source_xs;
    }

    public void addSource_x(Source_x source_x) {
        this.source_xs.add(source_x);
    }

}