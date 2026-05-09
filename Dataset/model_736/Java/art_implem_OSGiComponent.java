





import java.util.List;
import java.util.ArrayList;

public class art_implem_OSGiComponent extends ComponentImplementation {

    private String implementingClass;



    public art_implem_OSGiComponent(
        String implementingClass    ) {
        super(
        );
        this.implementingClass = implementingClass;
    }


    public String getImplementingclass() {
        return implementingClass;
    }

    public void setImplementingclass(String implementingClass) {
        this.implementingClass = implementingClass;
    }


}