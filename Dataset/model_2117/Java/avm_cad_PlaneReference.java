





import java.util.List;
import java.util.ArrayList;

public class avm_cad_PlaneReference  {






    private List<Plane> planes;


    public avm_cad_PlaneReference(
    ) {
        this.planes = new ArrayList<>();
    }

    public avm_cad_PlaneReference(
        ArrayList<Plane> planes    ) {
        this.planes = planes;
    }


    public List<Plane> getPlanes() {
        return planes;
    }

    public void addPlane(Plane plane) {
        this.planes.add(plane);
    }

}