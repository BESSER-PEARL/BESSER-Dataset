





import java.util.List;
import java.util.ArrayList;

public class Currency1  {

    private String name;
    private String id;
    private String abr;





    private Bill bill;


    public Currency1(
        String name,        String id,        String abr    ) {
        this.name = name;
        this.id = id;
        this.abr = abr;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getAbr() {
        return abr;
    }

    public void setAbr(String abr) {
        this.abr = abr;
    }

    public Bill getBill() {
        return bill;
    }

    public void setBill(Bill bill) {
        this.bill = bill;
    }

}