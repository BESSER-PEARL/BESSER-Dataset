





import java.util.List;
import java.util.ArrayList;

public class tgg_AttrCondDef extends NamedElements {

    private boolean userDefined;





    private tgg_Schema tgg_schema;


    public tgg_AttrCondDef(
        boolean userDefined    ) {
        super(
        );
        this.userDefined = userDefined;
    }


    public boolean getUserdefined() {
        return userDefined;
    }

    public void setUserdefined(boolean userDefined) {
        this.userDefined = userDefined;
    }

    public tgg_Schema getTgg_schema() {
        return tgg_schema;
    }

    public void setTgg_schema(tgg_Schema tgg_schema) {
        this.tgg_schema = tgg_schema;
    }

}