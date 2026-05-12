





import java.util.List;
import java.util.ArrayList;

public class scxmlxt_VarDef extends Typed {

    private String name;





    private scxmlxt_AbstractState scxmlxt_abstractstate;


    public scxmlxt_VarDef(
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

    public scxmlxt_AbstractState getScxmlxt_abstractstate() {
        return scxmlxt_abstractstate;
    }

    public void setScxmlxt_abstractstate(scxmlxt_AbstractState scxmlxt_abstractstate) {
        this.scxmlxt_abstractstate = scxmlxt_abstractstate;
    }

}