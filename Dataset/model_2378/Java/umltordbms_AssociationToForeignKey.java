





import java.util.List;
import java.util.ArrayList;

public class umltordbms_AssociationToForeignKey extends ToColumn {

    private String name;



    public umltordbms_AssociationToForeignKey(
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