





import java.util.List;
import java.util.ArrayList;

public class basecs_PackageOwnerCS extends ModelElementCS {






    private List<basecs_PackageCS> basecs_packagecss;


    public basecs_PackageOwnerCS(
    ) {
        super(
        );
        this.basecs_packagecss = new ArrayList<>();
    }

    public basecs_PackageOwnerCS(
        ArrayList<basecs_PackageCS> basecs_packagecss    ) {
        this.basecs_packagecss = basecs_packagecss;
    }


    public List<basecs_PackageCS> getBasecs_packagecss() {
        return basecs_packagecss;
    }

    public void addBasecs_packagecs(Basecs_packagecs basecs_packagecs) {
        this.basecs_packagecss.add(basecs_packagecs);
    }

}