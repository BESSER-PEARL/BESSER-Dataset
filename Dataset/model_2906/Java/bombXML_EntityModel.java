





import java.util.List;
import java.util.ArrayList;

public class bombXML_EntityModel  {






    private List<bombXML_Type> bombxml_types;


    public bombXML_EntityModel(
    ) {
        this.bombxml_types = new ArrayList<>();
    }

    public bombXML_EntityModel(
        ArrayList<bombXML_Type> bombxml_types    ) {
        this.bombxml_types = bombxml_types;
    }


    public List<bombXML_Type> getBombxml_types() {
        return bombxml_types;
    }

    public void addBombxml_type(Bombxml_type bombxml_type) {
        this.bombxml_types.add(bombxml_type);
    }

}