





import java.util.List;
import java.util.ArrayList;

public class uppaallite_TemplateType  {

    private String name;
    private String declaration;





    private uppaallite_TransitionType uppaallite_transitiontype;




    private List<uppaallite_TransitionType> uppaallite_transitiontypes;




    private uppaallite_LocationType uppaallite_locationtype;




    private uppaallite_UppaalDiagram uppaallite_uppaaldiagram;




    private List<uppaallite_LocationType> uppaallite_locationtypes;


    public uppaallite_TemplateType(
        String name,        String declaration    ) {
        this.name = name;
        this.declaration = declaration;
        this.uppaallite_transitiontypes = new ArrayList<>();
        this.uppaallite_locationtypes = new ArrayList<>();
    }

    public uppaallite_TemplateType(
        String name,        String declaration        ArrayList<uppaallite_TransitionType> uppaallite_transitiontypes,        ArrayList<uppaallite_LocationType> uppaallite_locationtypes    ) {
        this.name = name;
        this.declaration = declaration;
        this.uppaallite_transitiontypes = uppaallite_transitiontypes;
        this.uppaallite_locationtypes = uppaallite_locationtypes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDeclaration() {
        return declaration;
    }

    public void setDeclaration(String declaration) {
        this.declaration = declaration;
    }

    public uppaallite_TransitionType getUppaallite_transitiontype() {
        return uppaallite_transitiontype;
    }

    public void setUppaallite_transitiontype(uppaallite_TransitionType uppaallite_transitiontype) {
        this.uppaallite_transitiontype = uppaallite_transitiontype;
    }
    public List<uppaallite_TransitionType> getUppaallite_transitiontypes() {
        return uppaallite_transitiontypes;
    }

    public void addUppaallite_transitiontype(Uppaallite_transitiontype uppaallite_transitiontype) {
        this.uppaallite_transitiontypes.add(uppaallite_transitiontype);
    }
    public uppaallite_LocationType getUppaallite_locationtype() {
        return uppaallite_locationtype;
    }

    public void setUppaallite_locationtype(uppaallite_LocationType uppaallite_locationtype) {
        this.uppaallite_locationtype = uppaallite_locationtype;
    }
    public uppaallite_UppaalDiagram getUppaallite_uppaaldiagram() {
        return uppaallite_uppaaldiagram;
    }

    public void setUppaallite_uppaaldiagram(uppaallite_UppaalDiagram uppaallite_uppaaldiagram) {
        this.uppaallite_uppaaldiagram = uppaallite_uppaaldiagram;
    }
    public List<uppaallite_LocationType> getUppaallite_locationtypes() {
        return uppaallite_locationtypes;
    }

    public void addUppaallite_locationtype(Uppaallite_locationtype uppaallite_locationtype) {
        this.uppaallite_locationtypes.add(uppaallite_locationtype);
    }

}