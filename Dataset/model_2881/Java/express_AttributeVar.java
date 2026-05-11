





import java.util.List;
import java.util.ArrayList;

public class express_AttributeVar extends VarOrAttrib {






    private List<express_VarOrAttrib> express_varorattribs;


    public express_AttributeVar(
    ) {
        super(
        );
        this.express_varorattribs = new ArrayList<>();
    }

    public express_AttributeVar(
        ArrayList<express_VarOrAttrib> express_varorattribs    ) {
        this.express_varorattribs = express_varorattribs;
    }


    public List<express_VarOrAttrib> getExpress_varorattribs() {
        return express_varorattribs;
    }

    public void addExpress_varorattrib(Express_varorattrib express_varorattrib) {
        this.express_varorattribs.add(express_varorattrib);
    }

}