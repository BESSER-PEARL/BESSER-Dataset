





import java.util.List;
import java.util.ArrayList;

public class emig_Parameter extends LocatedElement {

    private String name;





    private emig_setterDef emig_setterdef;


    public emig_Parameter(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public emig_setterDef getEmig_setterdef() {
        return emig_setterdef;
    }

    public void setEmig_setterdef(emig_setterDef emig_setterdef) {
        this.emig_setterdef = emig_setterdef;
    }

}