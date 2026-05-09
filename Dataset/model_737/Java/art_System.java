





import java.util.List;
import java.util.ArrayList;

public class art_System extends ModelElement {






    private List<ComponentType> componenttypes;




    private List<art_DataType> art_datatypes;




    private List<Group> groups;


    public art_System(
    ) {
        super(
        );
        this.componenttypes = new ArrayList<>();
        this.art_datatypes = new ArrayList<>();
        this.groups = new ArrayList<>();
    }

    public art_System(
        ArrayList<ComponentType> componenttypes,        ArrayList<art_DataType> art_datatypes,        ArrayList<Group> groups    ) {
        this.componenttypes = componenttypes;
        this.art_datatypes = art_datatypes;
        this.groups = groups;
    }


    public List<ComponentType> getComponenttypes() {
        return componenttypes;
    }

    public void addComponenttype(Componenttype componenttype) {
        this.componenttypes.add(componenttype);
    }
    public List<art_DataType> getArt_datatypes() {
        return art_datatypes;
    }

    public void addArt_datatype(Art_datatype art_datatype) {
        this.art_datatypes.add(art_datatype);
    }
    public List<Group> getGroups() {
        return groups;
    }

    public void addGroup(Group group) {
        this.groups.add(group);
    }

}