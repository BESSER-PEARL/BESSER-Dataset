





import java.util.List;
import java.util.ArrayList;

public class Conge  {

    private String datedebut;
    private String adresse;
    private int id;
    private String datefin;





    private List<Employ_> employ_s;




    private List<salari_> salari_s;


    public Conge(
        String datedebut,        String adresse,        int id,        String datefin    ) {
        this.datedebut = datedebut;
        this.adresse = adresse;
        this.id = id;
        this.datefin = datefin;
        this.employ_s = new ArrayList<>();
        this.salari_s = new ArrayList<>();
    }

    public Conge(
        String datedebut,        String adresse,        int id,        String datefin        ArrayList<Employ_> employ_s,        ArrayList<salari_> salari_s    ) {
        this.datedebut = datedebut;
        this.adresse = adresse;
        this.id = id;
        this.datefin = datefin;
        this.employ_s = employ_s;
        this.salari_s = salari_s;
    }

    public String getDatedebut() {
        return datedebut;
    }

    public void setDatedebut(String datedebut) {
        this.datedebut = datedebut;
    }
    public String getAdresse() {
        return adresse;
    }

    public void setAdresse(String adresse) {
        this.adresse = adresse;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getDatefin() {
        return datefin;
    }

    public void setDatefin(String datefin) {
        this.datefin = datefin;
    }

    public List<Employ_> getEmploy_s() {
        return employ_s;
    }

    public void addEmploy_(Employ_ employ_) {
        this.employ_s.add(employ_);
    }
    public List<salari_> getSalari_s() {
        return salari_s;
    }

    public void addSalari_(Salari_ salari_) {
        this.salari_s.add(salari_);
    }

}