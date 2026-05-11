





import java.util.List;
import java.util.ArrayList;

public class nabla_Connectivity  {

    private String name;





    private nabla_ItemType nabla_itemtype;




    private nabla_NablaModule nabla_nablamodule;




    private List<nabla_ItemType> nabla_itemtypes;


    public nabla_Connectivity(
        String name    ) {
        this.name = name;
        this.nabla_itemtypes = new ArrayList<>();
    }

    public nabla_Connectivity(
        String name        ArrayList<nabla_ItemType> nabla_itemtypes    ) {
        this.name = name;
        this.nabla_itemtypes = nabla_itemtypes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public nabla_ItemType getNabla_itemtype() {
        return nabla_itemtype;
    }

    public void setNabla_itemtype(nabla_ItemType nabla_itemtype) {
        this.nabla_itemtype = nabla_itemtype;
    }
    public nabla_NablaModule getNabla_nablamodule() {
        return nabla_nablamodule;
    }

    public void setNabla_nablamodule(nabla_NablaModule nabla_nablamodule) {
        this.nabla_nablamodule = nabla_nablamodule;
    }
    public List<nabla_ItemType> getNabla_itemtypes() {
        return nabla_itemtypes;
    }

    public void addNabla_itemtype(Nabla_itemtype nabla_itemtype) {
        this.nabla_itemtypes.add(nabla_itemtype);
    }

}