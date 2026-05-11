





import java.util.List;
import java.util.ArrayList;

public class fiacre_Profile extends Channel {






    private List<fiacre_Type> fiacre_types;


    public fiacre_Profile(
    ) {
        super(
        );
        this.fiacre_types = new ArrayList<>();
    }

    public fiacre_Profile(
        ArrayList<fiacre_Type> fiacre_types    ) {
        this.fiacre_types = fiacre_types;
    }


    public List<fiacre_Type> getFiacre_types() {
        return fiacre_types;
    }

    public void addFiacre_type(Fiacre_type fiacre_type) {
        this.fiacre_types.add(fiacre_type);
    }

}