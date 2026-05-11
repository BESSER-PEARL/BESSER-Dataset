





import java.util.List;
import java.util.ArrayList;

public class di_Diagram extends ContainerShape {






    private List<di_Link> di_links;


    public di_Diagram(
    ) {
        super(
        );
        this.di_links = new ArrayList<>();
    }

    public di_Diagram(
        ArrayList<di_Link> di_links    ) {
        this.di_links = di_links;
    }


    public List<di_Link> getDi_links() {
        return di_links;
    }

    public void addDi_link(Di_link di_link) {
        this.di_links.add(di_link);
    }

}