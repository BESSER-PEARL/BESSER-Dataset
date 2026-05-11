





import java.util.List;
import java.util.ArrayList;

public class netModel_IntrinsicType extends Type {

    private String id;





    private netModel_SimpleMember netmodel_simplemember;


    public netModel_IntrinsicType(
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

    public netModel_SimpleMember getNetmodel_simplemember() {
        return netmodel_simplemember;
    }

    public void setNetmodel_simplemember(netModel_SimpleMember netmodel_simplemember) {
        this.netmodel_simplemember = netmodel_simplemember;
    }

}