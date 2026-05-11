





import java.util.List;
import java.util.ArrayList;

public class dmx_DmxStaticReference extends DExpression {

    private boolean plural;
    private String displayName;



    public dmx_DmxStaticReference(
        boolean plural,        String displayName    ) {
        super(
        );
        this.plural = plural;
        this.displayName = displayName;
    }


    public boolean getPlural() {
        return plural;
    }

    public void setPlural(boolean plural) {
        this.plural = plural;
    }
    public String getDisplayname() {
        return displayName;
    }

    public void setDisplayname(String displayName) {
        this.displayName = displayName;
    }


}