





import java.util.List;
import java.util.ArrayList;

public class diva_Variant extends ModelContainer, NamedElement {

    private String weaveLevel;





    private diva_Dimension diva_dimension;




    private diva_Dimension diva_dimension;


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

    public diva_Dimension getDiva_dimension() {
        return diva_dimension;
    }

    public void setDiva_dimension(diva_Dimension diva_dimension) {
        this.diva_dimension = diva_dimension;
    }
    public diva_Dimension getDiva_dimension() {
        return diva_dimension;
    }

    public void setDiva_dimension(diva_Dimension diva_dimension) {
        this.diva_dimension = diva_dimension;
    }

}