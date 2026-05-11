





import java.util.List;
import java.util.ArrayList;

public class railDsl_Track extends Declaration {






    private List<railDsl_TrackObject> raildsl_trackobjects;


    public railDsl_Track(
    ) {
        super(
        );
        this.raildsl_trackobjects = new ArrayList<>();
    }

    public railDsl_Track(
        ArrayList<railDsl_TrackObject> raildsl_trackobjects    ) {
        this.raildsl_trackobjects = raildsl_trackobjects;
    }


    public List<railDsl_TrackObject> getRaildsl_trackobjects() {
        return raildsl_trackobjects;
    }

    public void addRaildsl_trackobject(Raildsl_trackobject raildsl_trackobject) {
        this.raildsl_trackobjects.add(raildsl_trackobject);
    }

}