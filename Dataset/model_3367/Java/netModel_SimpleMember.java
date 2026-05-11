





import java.util.List;
import java.util.ArrayList;

public class netModel_SimpleMember  {

    private String name;





    private netModel_SimpleMemberAssignment netmodel_simplememberassignment;


    public netModel_SimpleMember(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public netModel_SimpleMemberAssignment getNetmodel_simplememberassignment() {
        return netmodel_simplememberassignment;
    }

    public void setNetmodel_simplememberassignment(netModel_SimpleMemberAssignment netmodel_simplememberassignment) {
        this.netmodel_simplememberassignment = netmodel_simplememberassignment;
    }

}