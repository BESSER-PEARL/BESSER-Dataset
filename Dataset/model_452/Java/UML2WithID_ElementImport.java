





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_ElementImport extends DirectedRelationship {

    private String visibility;
    private String alias;



    public UML2WithID_ElementImport(
        String visibility,        String alias    ) {
        super(
        );
        this.visibility = visibility;
        this.alias = alias;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }


}