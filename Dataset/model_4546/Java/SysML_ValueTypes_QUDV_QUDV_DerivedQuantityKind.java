





import java.util.List;
import java.util.ArrayList;

public class SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind extends QuantityKind {






    private List<QuantityKindFactor> quantitykindfactors;


    public SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind(
    ) {
        super(
        );
        this.quantitykindfactors = new ArrayList<>();
    }

    public SysML_ValueTypes_QUDV_QUDV_DerivedQuantityKind(
        ArrayList<QuantityKindFactor> quantitykindfactors    ) {
        this.quantitykindfactors = quantitykindfactors;
    }


    public List<QuantityKindFactor> getQuantitykindfactors() {
        return quantitykindfactors;
    }

    public void addQuantitykindfactor(Quantitykindfactor quantitykindfactor) {
        this.quantitykindfactors.add(quantitykindfactor);
    }

}