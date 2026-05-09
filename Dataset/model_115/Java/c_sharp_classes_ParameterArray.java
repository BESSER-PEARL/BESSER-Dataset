





import java.util.List;
import java.util.ArrayList;

public class c_sharp_classes_ParameterArray  {






    private List<Attributes> attributess;




    private Identifier identifier;


    public c_sharp_classes_ParameterArray(
    ) {
        this.attributess = new ArrayList<>();
    }

    public c_sharp_classes_ParameterArray(
        ArrayList<Attributes> attributess    ) {
        this.attributess = attributess;
    }


    public List<Attributes> getAttributess() {
        return attributess;
    }

    public void addAttributes(Attributes attributes) {
        this.attributess.add(attributes);
    }
    public Identifier getIdentifier() {
        return identifier;
    }

    public void setIdentifier(Identifier identifier) {
        this.identifier = identifier;
    }

}