





import java.util.List;
import java.util.ArrayList;

public class fopramodel_FoPraManagementSystem  {






    private List<fopramodel_FoPra> fopramodel_fopras;


    public fopramodel_FoPraManagementSystem(
    ) {
        this.fopramodel_fopras = new ArrayList<>();
    }

    public fopramodel_FoPraManagementSystem(
        ArrayList<fopramodel_FoPra> fopramodel_fopras    ) {
        this.fopramodel_fopras = fopramodel_fopras;
    }


    public List<fopramodel_FoPra> getFopramodel_fopras() {
        return fopramodel_fopras;
    }

    public void addFopramodel_fopra(Fopramodel_fopra fopramodel_fopra) {
        this.fopramodel_fopras.add(fopramodel_fopra);
    }

}