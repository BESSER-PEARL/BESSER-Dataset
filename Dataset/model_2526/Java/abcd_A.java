





import java.util.List;
import java.util.ArrayList;

public class abcd_A extends NamedElt {

    private String aBooleanAttr;
    private int anIntegerAttr;





    private abcd_Model abcd_model;




    private List<abcd_A> abcd_as;




    private abcd_Model abcd_model;


    public abcd_A(
        String aBooleanAttr,        int anIntegerAttr    ) {
        super(
        );
        this.aBooleanAttr = aBooleanAttr;
        this.anIntegerAttr = anIntegerAttr;
        this.abcd_as = new ArrayList<>();
    }

    public abcd_A(
        String aBooleanAttr,        int anIntegerAttr        ArrayList<abcd_A> abcd_as    ) {
        this.aBooleanAttr = aBooleanAttr;
        this.anIntegerAttr = anIntegerAttr;
        this.abcd_as = abcd_as;
    }

    public String getAbooleanattr() {
        return aBooleanAttr;
    }

    public void setAbooleanattr(String aBooleanAttr) {
        this.aBooleanAttr = aBooleanAttr;
    }
    public int getAnintegerattr() {
        return anIntegerAttr;
    }

    public void setAnintegerattr(int anIntegerAttr) {
        this.anIntegerAttr = anIntegerAttr;
    }

    public abcd_Model getAbcd_model() {
        return abcd_model;
    }

    public void setAbcd_model(abcd_Model abcd_model) {
        this.abcd_model = abcd_model;
    }
    public List<abcd_A> getAbcd_as() {
        return abcd_as;
    }

    public void addAbcd_a(Abcd_a abcd_a) {
        this.abcd_as.add(abcd_a);
    }
    public abcd_Model getAbcd_model() {
        return abcd_model;
    }

    public void setAbcd_model(abcd_Model abcd_model) {
        this.abcd_model = abcd_model;
    }

}