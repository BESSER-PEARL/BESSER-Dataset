





import java.util.List;
import java.util.ArrayList;

public class Procedure  {

    private int idProcedure;
    private int price;
    private String name;





    private List<Treatment> treatments;


    public Procedure(
        int idProcedure,        int price,        String name    ) {
        this.idProcedure = idProcedure;
        this.price = price;
        this.name = name;
        this.treatments = new ArrayList<>();
    }

    public Procedure(
        int idProcedure,        int price,        String name        ArrayList<Treatment> treatments    ) {
        this.idProcedure = idProcedure;
        this.price = price;
        this.name = name;
        this.treatments = treatments;
    }

    public int getIdprocedure() {
        return idProcedure;
    }

    public void setIdprocedure(int idProcedure) {
        this.idProcedure = idProcedure;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Treatment> getTreatments() {
        return treatments;
    }

    public void addTreatment(Treatment treatment) {
        this.treatments.add(treatment);
    }

}