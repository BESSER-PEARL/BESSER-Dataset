





import java.util.List;
import java.util.ArrayList;

public class typecong_  {

    private int idconge;





    private List<Conge> conges;


    public typecong_(
        int idconge    ) {
        this.idconge = idconge;
        this.conges = new ArrayList<>();
    }

    public typecong_(
        int idconge        ArrayList<Conge> conges    ) {
        this.idconge = idconge;
        this.conges = conges;
    }

    public int getIdconge() {
        return idconge;
    }

    public void setIdconge(int idconge) {
        this.idconge = idconge;
    }

    public List<Conge> getConges() {
        return conges;
    }

    public void addConge(Conge conge) {
        this.conges.add(conge);
    }

}