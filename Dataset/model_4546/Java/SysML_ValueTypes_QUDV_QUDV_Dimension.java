





import java.util.List;
import java.util.ArrayList;

public class SysML_ValueTypes_QUDV_QUDV_Dimension  {

    private String name;





    private List<QuantityKindFactor> quantitykindfactors;


    public SysML_ValueTypes_QUDV_QUDV_Dimension(
        String name    ) {
        this.name = name;
        this.quantitykindfactors = new ArrayList<>();
    }

    public SysML_ValueTypes_QUDV_QUDV_Dimension(
        String name        ArrayList<QuantityKindFactor> quantitykindfactors    ) {
        this.name = name;
        this.quantitykindfactors = quantitykindfactors;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<QuantityKindFactor> getQuantitykindfactors() {
        return quantitykindfactors;
    }

    public void addQuantitykindfactor(Quantitykindfactor quantitykindfactor) {
        this.quantitykindfactors.add(quantitykindfactor);
    }

}