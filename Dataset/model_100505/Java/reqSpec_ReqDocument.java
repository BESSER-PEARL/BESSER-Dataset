





import java.util.List;
import java.util.ArrayList;

public class reqSpec_ReqDocument extends ReqRoot {






    private List<reqSpec_EObject> reqspec_eobjects;


    public reqSpec_ReqDocument(
    ) {
        super(
        );
        this.reqspec_eobjects = new ArrayList<>();
    }

    public reqSpec_ReqDocument(
        ArrayList<reqSpec_EObject> reqspec_eobjects    ) {
        this.reqspec_eobjects = reqspec_eobjects;
    }


    public List<reqSpec_EObject> getReqspec_eobjects() {
        return reqspec_eobjects;
    }

    public void addReqspec_eobject(Reqspec_eobject reqspec_eobject) {
        this.reqspec_eobjects.add(reqspec_eobject);
    }

}