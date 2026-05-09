





import java.util.List;
import java.util.ArrayList;

public class oaam_common_AttributeReference extends AttributeA {






    private List<OaamBaseElementA> oaambaseelementas;


    public oaam_common_AttributeReference(
    ) {
        super(
        );
        this.oaambaseelementas = new ArrayList<>();
    }

    public oaam_common_AttributeReference(
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