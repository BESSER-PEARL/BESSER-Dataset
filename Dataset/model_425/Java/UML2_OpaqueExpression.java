





import java.util.List;
import java.util.ArrayList;

public class UML2_OpaqueExpression extends ValueSpecification {

    private String bodies;
    private String language;



    public UML2_OpaqueExpression(
        String bodies,        String language    ) {
        super(
        );
        this.bodies = bodies;
        this.language = language;
    }


    public String getBodies() {
        return bodies;
    }

    public void setBodies(String bodies) {
        this.bodies = bodies;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }


}