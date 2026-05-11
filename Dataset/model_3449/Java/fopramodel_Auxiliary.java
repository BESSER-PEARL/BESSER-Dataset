





import java.util.List;
import java.util.ArrayList;

public class fopramodel_Auxiliary  {

    private String description;
    private String kind;





    private List<fopramodel_FoPra> fopramodel_fopras;




    private fopramodel_FoPra fopramodel_fopra;




    private fopramodel_FoPraManagementSystem fopramodel_fopramanagementsystem;


    public fopramodel_Auxiliary(
        String description,        String kind    ) {
        this.description = description;
        this.kind = kind;
        this.fopramodel_fopras = new ArrayList<>();
    }

    public fopramodel_Auxiliary(
        String description,        String kind        ArrayList<fopramodel_FoPra> fopramodel_fopras    ) {
        this.description = description;
        this.kind = kind;
        this.fopramodel_fopras = fopramodel_fopras;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
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
    public fopramodel_FoPraManagementSystem getFopramodel_fopramanagementsystem() {
        return fopramodel_fopramanagementsystem;
    }

    public void setFopramodel_fopramanagementsystem(fopramodel_FoPraManagementSystem fopramodel_fopramanagementsystem) {
        this.fopramodel_fopramanagementsystem = fopramodel_fopramanagementsystem;
    }

}