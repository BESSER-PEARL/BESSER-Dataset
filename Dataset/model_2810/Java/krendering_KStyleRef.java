





import java.util.List;
import java.util.ArrayList;

public class krendering_KStyleRef extends KStyle {

    private String referencedTypes;





    private krendering_KStyleHolder krendering_kstyleholder;


    public krendering_KStyleRef(
        String referencedTypes    ) {
        super(
        );
        this.referencedTypes = referencedTypes;
    }


    public String getReferencedtypes() {
        return referencedTypes;
    }

    public void setReferencedtypes(String referencedTypes) {
        this.referencedTypes = referencedTypes;
    }

    public krendering_KStyleHolder getKrendering_kstyleholder() {
        return krendering_kstyleholder;
    }

    public void setKrendering_kstyleholder(krendering_KStyleHolder krendering_kstyleholder) {
        this.krendering_kstyleholder = krendering_kstyleholder;
    }

}