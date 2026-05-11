





import java.util.List;
import java.util.ArrayList;

public class fopramodel_Student extends Person {

    private String course;
    private String matrikel;





    private fopramodel_FoPra fopramodel_fopra;




    private List<fopramodel_FoPra> fopramodel_fopras;


    public fopramodel_Student(
        String course,        String matrikel    ) {
        super(
        );
        this.course = course;
        this.matrikel = matrikel;
        this.fopramodel_fopras = new ArrayList<>();
    }

    public fopramodel_Student(
        String course,        String matrikel        ArrayList<fopramodel_FoPra> fopramodel_fopras    ) {
        this.course = course;
        this.matrikel = matrikel;
        this.fopramodel_fopras = fopramodel_fopras;
    }

    public String getCourse() {
        return course;
    }

    public void setCourse(String course) {
        this.course = course;
    }
    public String getMatrikel() {
        return matrikel;
    }

    public void setMatrikel(String matrikel) {
        this.matrikel = matrikel;
    }

    public fopramodel_FoPra getFopramodel_fopra() {
        return fopramodel_fopra;
    }

    public void setFopramodel_fopra(fopramodel_FoPra fopramodel_fopra) {
        this.fopramodel_fopra = fopramodel_fopra;
    }
    public List<fopramodel_FoPra> getFopramodel_fopras() {
        return fopramodel_fopras;
    }

    public void addFopramodel_fopra(Fopramodel_fopra fopramodel_fopra) {
        this.fopramodel_fopras.add(fopramodel_fopra);
    }

}