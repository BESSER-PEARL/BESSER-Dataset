





import java.util.List;
import java.util.ArrayList;

public class MARTE_HwLayout_HwComponent extends HwResource {

    private String kind;





    private NFP_Real nfp_real;




    private List<NFP_Natural> nfp_naturals;




    private NFP_Power nfp_power;




    private NFP_Natural nfp_natural;




    private NFP_Power nfp_power;


    public MARTE_HwLayout_HwComponent(
        String kind    ) {
        super(
        );
        this.kind = kind;
        this.nfp_naturals = new ArrayList<>();
    }

    public MARTE_HwLayout_HwComponent(
        String kind        ArrayList<NFP_Natural> nfp_naturals    ) {
        this.kind = kind;
        this.nfp_naturals = nfp_naturals;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public NFP_Real getNfp_real() {
        return nfp_real;
    }

    public void setNfp_real(NFP_Real nfp_real) {
        this.nfp_real = nfp_real;
    }
    public List<NFP_Natural> getNfp_naturals() {
        return nfp_naturals;
    }

    public void addNfp_natural(Nfp_natural nfp_natural) {
        this.nfp_naturals.add(nfp_natural);
    }
    public NFP_Power getNfp_power() {
        return nfp_power;
    }

    public void setNfp_power(NFP_Power nfp_power) {
        this.nfp_power = nfp_power;
    }
    public NFP_Natural getNfp_natural() {
        return nfp_natural;
    }

    public void setNfp_natural(NFP_Natural nfp_natural) {
        this.nfp_natural = nfp_natural;
    }
    public NFP_Power getNfp_power() {
        return nfp_power;
    }

    public void setNfp_power(NFP_Power nfp_power) {
        this.nfp_power = nfp_power;
    }

}