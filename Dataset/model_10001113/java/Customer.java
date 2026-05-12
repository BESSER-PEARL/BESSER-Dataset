





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int numFemale;
    private None type;
    private int numMale;





    private Table table;


    public Customer(
        int numFemale,        None type,        int numMale    ) {
        this.numFemale = numFemale;
        this.type = type;
        this.numMale = numMale;
    }


    public int getNumfemale() {
        return numFemale;
    }

    public void setNumfemale(int numFemale) {
        this.numFemale = numFemale;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public int getNummale() {
        return numMale;
    }

    public void setNummale(int numMale) {
        this.numMale = numMale;
    }

    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }

}