





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_RepresentationTemplate  {

    private String name;





    private List<RepresentationDescription> representationdescriptions;


    public viewpoint_description_RepresentationTemplate(
        String name    ) {
        this.name = name;
        this.representationdescriptions = new ArrayList<>();
    }

    public viewpoint_description_RepresentationTemplate(
        String name        ArrayList<RepresentationDescription> representationdescriptions    ) {
        this.name = name;
        this.representationdescriptions = representationdescriptions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<RepresentationDescription> getRepresentationdescriptions() {
        return representationdescriptions;
    }

    public void addRepresentationdescription(Representationdescription representationdescription) {
        this.representationdescriptions.add(representationdescription);
    }

}