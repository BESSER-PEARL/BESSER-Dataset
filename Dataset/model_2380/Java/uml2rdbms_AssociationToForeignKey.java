





import java.util.List;
import java.util.ArrayList;

public class uml2rdbms_AssociationToForeignKey extends ToColumn {

    private String name;



    public uml2rdbms_AssociationToForeignKey(
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


}