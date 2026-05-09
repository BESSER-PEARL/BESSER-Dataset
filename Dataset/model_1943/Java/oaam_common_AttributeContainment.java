





import java.util.List;
import java.util.ArrayList;

public class oaam_common_AttributeContainment extends AttributeA {






    private List<OaamBaseElementA> oaambaseelementas;


    public oaam_common_AttributeContainment(
    ) {
        super(
        );
        this.oaambaseelementas = new ArrayList<>();
    }

    public oaam_common_AttributeContainment(
        ArrayList<OaamBaseElementA> oaambaseelementas    ) {
        this.oaambaseelementas = oaambaseelementas;
    }


    public List<OaamBaseElementA> getOaambaseelementas() {
        return oaambaseelementas;
    }

    public void addOaambaseelementa(Oaambaseelementa oaambaseelementa) {
        this.oaambaseelementas.add(oaambaseelementa);
    }

}