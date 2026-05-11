





import java.util.List;
import java.util.ArrayList;

public class fopramodel_ResearchGroup  {

    private String name;





    private List<fopramodel_FoPra> fopramodel_fopras;




    private fopramodel_Associate fopramodel_associate;




    private fopramodel_Professor fopramodel_professor;




    private fopramodel_Professor fopramodel_professor;




    private List<fopramodel_Associate> fopramodel_associates;




    private fopramodel_FoPra fopramodel_fopra;


    public fopramodel_ResearchGroup(
        String name    ) {
        this.name = name;
        this.fopramodel_fopras = new ArrayList<>();
        this.fopramodel_associates = new ArrayList<>();
    }

    public fopramodel_ResearchGroup(
        String name        ArrayList<fopramodel_FoPra> fopramodel_fopras,        ArrayList<fopramodel_Associate> fopramodel_associates    ) {
        this.name = name;
        this.fopramodel_fopras = fopramodel_fopras;
        this.fopramodel_associates = fopramodel_associates;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<fopramodel_FoPra> getFopramodel_fopras() {
        return fopramodel_fopras;
    }

    public void addFopramodel_fopra(Fopramodel_fopra fopramodel_fopra) {
        this.fopramodel_fopras.add(fopramodel_fopra);
    }
    public fopramodel_Associate getFopramodel_associate() {
        return fopramodel_associate;
    }

    public void setFopramodel_associate(fopramodel_Associate fopramodel_associate) {
        this.fopramodel_associate = fopramodel_associate;
    }
    public fopramodel_Professor getFopramodel_professor() {
        return fopramodel_professor;
    }

    public void setFopramodel_professor(fopramodel_Professor fopramodel_professor) {
        this.fopramodel_professor = fopramodel_professor;
    }
    public fopramodel_Professor getFopramodel_professor() {
        return fopramodel_professor;
    }

    public void setFopramodel_professor(fopramodel_Professor fopramodel_professor) {
        this.fopramodel_professor = fopramodel_professor;
    }
    public List<fopramodel_Associate> getFopramodel_associates() {
        return fopramodel_associates;
    }

    public void addFopramodel_associate(Fopramodel_associate fopramodel_associate) {
        this.fopramodel_associates.add(fopramodel_associate);
    }
    public fopramodel_FoPra getFopramodel_fopra() {
        return fopramodel_fopra;
    }

    public void setFopramodel_fopra(fopramodel_FoPra fopramodel_fopra) {
        this.fopramodel_fopra = fopramodel_fopra;
    }

}