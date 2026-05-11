





import java.util.List;
import java.util.ArrayList;

public class camel_scalability_FunctionalEvent extends SimpleEvent {

    private String functionalType;



    public camel_scalability_FunctionalEvent(
        String functionalType    ) {
        super(
        );
        this.functionalType = functionalType;
    }


    public String getFunctionaltype() {
        return functionalType;
    }

    public void setFunctionaltype(String functionalType) {
        this.functionalType = functionalType;
    }


}