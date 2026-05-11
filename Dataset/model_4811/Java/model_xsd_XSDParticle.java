





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDParticle extends XSDComplexTypeContent {

    private int maxOccurs;
    private int minOccurs;



    public model_xsd_XSDParticle(
        int maxOccurs,        int minOccurs    ) {
        super(
        );
        this.maxOccurs = maxOccurs;
        this.minOccurs = minOccurs;
    }


    public int getMaxoccurs() {
        return maxOccurs;
    }

    public void setMaxoccurs(int maxOccurs) {
        this.maxOccurs = maxOccurs;
    }
    public int getMinoccurs() {
        return minOccurs;
    }

    public void setMinoccurs(int minOccurs) {
        this.minOccurs = minOccurs;
    }


}