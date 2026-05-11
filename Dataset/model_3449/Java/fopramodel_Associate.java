





import java.util.List;
import java.util.ArrayList;

public class fopramodel_Associate extends Person {






    private List<fopramodel_FoPra> fopramodel_fopras;




    private fopramodel_FoPra fopramodel_fopra;


    public fopramodel_Associate(
    ) {
        super(
        );
        this.fopramodel_fopras = new ArrayList<>();
    }

    public fopramodel_Associate(
        ArrayList<fopramodel_FoPra> fopramodel_fopras    ) {
        this.fopramodel_fopras = fopramodel_fopras;
    }


    public List<fopramodel_FoPra> getFopramodel_fopras() {
        return fopramodel_fopras;
    }

    public void addFopramodel_fopra(Fopramodel_fopra fopramodel_fopra) {
        this.fopramodel_fopras.add(fopramodel_fopra);
    }
    public fopramodel_FoPra getFopramodel_fopra() {
        return fopramodel_fopra;
    }

    public void setFopramodel_fopra(fopramodel_FoPra fopramodel_fopra) {
        this.fopramodel_fopra = fopramodel_fopra;
    }

}