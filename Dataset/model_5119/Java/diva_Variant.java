





import java.util.List;
import java.util.ArrayList;

public class diva_Variant extends ModelContainer, NamedElement {

    private String weaveLevel;



    public diva_Variant(
        String weaveLevel    ) {
        super(
        );
        this.weaveLevel = weaveLevel;
    }


    public String getWeavelevel() {
        return weaveLevel;
    }

    public void setWeavelevel(String weaveLevel) {
        this.weaveLevel = weaveLevel;
    }


}