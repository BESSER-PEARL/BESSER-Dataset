





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_Record extends DefinedType, ParameterDomain {

    private boolean isTuple;
    private String name;



    public OPLmetamodel_Record(
        boolean isTuple,        String name    ) {
        super(
        );
        this.isTuple = isTuple;
        this.name = name;
    }


    public boolean getIstuple() {
        return isTuple;
    }

    public void setIstuple(boolean isTuple) {
        this.isTuple = isTuple;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}