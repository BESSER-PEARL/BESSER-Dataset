





import java.util.List;
import java.util.ArrayList;

public class iso20022_MessageComponent extends MessageElementContainer {






    private iso20022_Xor iso20022_xor;




    private List<iso20022_Xor> iso20022_xors;


    public iso20022_MessageComponent(
    ) {
        super(
        );
        this.iso20022_xors = new ArrayList<>();
    }

    public iso20022_MessageComponent(
        ArrayList<iso20022_Xor> iso20022_xors    ) {
        this.iso20022_xors = iso20022_xors;
    }


    public iso20022_Xor getIso20022_xor() {
        return iso20022_xor;
    }

    public void setIso20022_xor(iso20022_Xor iso20022_xor) {
        this.iso20022_xor = iso20022_xor;
    }
    public List<iso20022_Xor> getIso20022_xors() {
        return iso20022_xors;
    }

    public void addIso20022_xor(Iso20022_xor iso20022_xor) {
        this.iso20022_xors.add(iso20022_xor);
    }

}