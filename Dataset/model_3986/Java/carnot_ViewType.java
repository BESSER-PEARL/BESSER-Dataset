





import java.util.List;
import java.util.ArrayList;

public class carnot_ViewType extends IExtensibleElement, IModelElement {

    private String name;





    private List<carnot_ViewType> carnot_viewtypes;


    public carnot_ViewType(
        String name    ) {
        super(
        );
        this.name = name;
        this.carnot_viewtypes = new ArrayList<>();
    }

    public carnot_ViewType(
        String name        ArrayList<carnot_ViewType> carnot_viewtypes    ) {
        this.name = name;
        this.carnot_viewtypes = carnot_viewtypes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<carnot_ViewType> getCarnot_viewtypes() {
        return carnot_viewtypes;
    }

    public void addCarnot_viewtype(Carnot_viewtype carnot_viewtype) {
        this.carnot_viewtypes.add(carnot_viewtype);
    }

}