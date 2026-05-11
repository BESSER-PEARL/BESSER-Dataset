





import java.util.List;
import java.util.ArrayList;

public class nabla_ConnectivityVar extends Var {






    private List<nabla_MultipleConnectivity> nabla_multipleconnectivitys;


    public nabla_ConnectivityVar(
    ) {
        super(
        );
        this.nabla_multipleconnectivitys = new ArrayList<>();
    }

    public nabla_ConnectivityVar(
        ArrayList<nabla_MultipleConnectivity> nabla_multipleconnectivitys    ) {
        this.nabla_multipleconnectivitys = nabla_multipleconnectivitys;
    }


    public List<nabla_MultipleConnectivity> getNabla_multipleconnectivitys() {
        return nabla_multipleconnectivitys;
    }

    public void addNabla_multipleconnectivity(Nabla_multipleconnectivity nabla_multipleconnectivity) {
        this.nabla_multipleconnectivitys.add(nabla_multipleconnectivity);
    }

}