





import java.util.List;
import java.util.ArrayList;

public class Supplier  {

    private String fax;
    private String num;





    private List<Supply> supplys;


    public Supplier(
        String fax,        String num    ) {
        this.fax = fax;
        this.num = num;
        this.supplys = new ArrayList<>();
    }

    public Supplier(
        String fax,        String num        ArrayList<Supply> supplys    ) {
        this.fax = fax;
        this.num = num;
        this.supplys = supplys;
    }

    public String getFax() {
        return fax;
    }

    public void setFax(String fax) {
        this.fax = fax;
    }
    public String getNum() {
        return num;
    }

    public void setNum(String num) {
        this.num = num;
    }

    public List<Supply> getSupplys() {
        return supplys;
    }

    public void addSupply(Supply supply) {
        this.supplys.add(supply);
    }

}