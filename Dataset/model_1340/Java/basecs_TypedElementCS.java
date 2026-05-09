





import java.util.List;
import java.util.ArrayList;

public class basecs_TypedElementCS extends NamedElementCS {

    private String qualifier;
    private boolean optional;



    public basecs_TypedElementCS(
        String qualifier,        boolean optional    ) {
        super(
        );
        this.qualifier = qualifier;
        this.optional = optional;
    }


    public String getQualifier() {
        return qualifier;
    }

    public void setQualifier(String qualifier) {
        this.qualifier = qualifier;
    }
    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }


}