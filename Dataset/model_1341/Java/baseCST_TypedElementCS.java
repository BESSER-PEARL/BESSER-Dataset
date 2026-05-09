





import java.util.List;
import java.util.ArrayList;

public class baseCST_TypedElementCS extends NamedElementCS {

    private String qualifier;
    private boolean optional;



    public baseCST_TypedElementCS(
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