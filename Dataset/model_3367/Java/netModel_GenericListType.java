





import java.util.List;
import java.util.ArrayList;

public class netModel_GenericListType extends Type {

    private String id;





    private netModel_Type netmodel_type;


    public netModel_GenericListType(
        String id    ) {
        super(
        );
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public netModel_Type getNetmodel_type() {
        return netmodel_type;
    }

    public void setNetmodel_type(netModel_Type netmodel_type) {
        this.netmodel_type = netmodel_type;
    }

}