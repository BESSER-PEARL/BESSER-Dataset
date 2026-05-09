





import java.util.List;
import java.util.ArrayList;

public class c_sharp_classes_FixedParameter  {






    private Identifier identifier;




    private List<Attributes> attributess;


    public c_sharp_classes_FixedParameter(
    ) {
        this.attributess = new ArrayList<>();
    }

    public c_sharp_classes_FixedParameter(
        ArrayList<Attributes> attributess    ) {
        this.attributess = attributess;
    }


    public Identifier getIdentifier() {
        return identifier;
    }

    public void setIdentifier(Identifier identifier) {
        this.identifier = identifier;
    }
    public List<Attributes> getAttributess() {
        return attributess;
    }

    public void addAttributes(Attributes attributes) {
        this.attributess.add(attributes);
    }

}