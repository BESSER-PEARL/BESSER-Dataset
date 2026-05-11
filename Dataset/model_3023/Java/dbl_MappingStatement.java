





import java.util.List;
import java.util.ArrayList;

public class dbl_MappingStatement extends Statement {






    private List<dbl_MappingPart> dbl_mappingparts;


    public dbl_MappingStatement(
    ) {
        super(
        );
        this.dbl_mappingparts = new ArrayList<>();
    }

    public dbl_MappingStatement(
        ArrayList<dbl_MappingPart> dbl_mappingparts    ) {
        this.dbl_mappingparts = dbl_mappingparts;
    }


    public List<dbl_MappingPart> getDbl_mappingparts() {
        return dbl_mappingparts;
    }

    public void addDbl_mappingpart(Dbl_mappingpart dbl_mappingpart) {
        this.dbl_mappingparts.add(dbl_mappingpart);
    }

}