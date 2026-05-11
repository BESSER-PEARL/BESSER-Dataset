





import java.util.List;
import java.util.ArrayList;

public class cmof_Expression extends ValueSpecification {






    private List<cmof_ValueSpecification> cmof_valuespecifications;


    public cmof_Expression(
    ) {
        super(
        );
        this.cmof_valuespecifications = new ArrayList<>();
    }

    public cmof_Expression(
        ArrayList<cmof_ValueSpecification> cmof_valuespecifications    ) {
        this.cmof_valuespecifications = cmof_valuespecifications;
    }


    public List<cmof_ValueSpecification> getCmof_valuespecifications() {
        return cmof_valuespecifications;
    }

    public void addCmof_valuespecification(Cmof_valuespecification cmof_valuespecification) {
        this.cmof_valuespecifications.add(cmof_valuespecification);
    }

}