





import java.util.List;
import java.util.ArrayList;

public class di_Diagram extends View {






    private List<di_Connector> di_connectors;


    public di_Diagram(
    ) {
        super(
        );
        this.di_connectors = new ArrayList<>();
    }

    public di_Diagram(
        ArrayList<di_Connector> di_connectors    ) {
        this.di_connectors = di_connectors;
    }


    public List<di_Connector> getDi_connectors() {
        return di_connectors;
    }

    public void addDi_connector(Di_connector di_connector) {
        this.di_connectors.add(di_connector);
    }

}