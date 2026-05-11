





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_SetType extends DefinedType, ParameterDomain {

    private String name;





    private OPLmetamodel_StateFunction oplmetamodel_statefunction;




    private OPLmetamodel_AbstractType oplmetamodel_abstracttype;


    public OPLmetamodel_SetType(
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

    public OPLmetamodel_StateFunction getOplmetamodel_statefunction() {
        return oplmetamodel_statefunction;
    }

    public void setOplmetamodel_statefunction(OPLmetamodel_StateFunction oplmetamodel_statefunction) {
        this.oplmetamodel_statefunction = oplmetamodel_statefunction;
    }
    public OPLmetamodel_AbstractType getOplmetamodel_abstracttype() {
        return oplmetamodel_abstracttype;
    }

    public void setOplmetamodel_abstracttype(OPLmetamodel_AbstractType oplmetamodel_abstracttype) {
        this.oplmetamodel_abstracttype = oplmetamodel_abstracttype;
    }

}