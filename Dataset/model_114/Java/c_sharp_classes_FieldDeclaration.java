





import java.util.List;
import java.util.ArrayList;

public class c_sharp_classes_FieldDeclaration extends ClassMemberDeclaration {






    private List<Attributes> attributess;




    private List<Modifier> modifiers;


    public c_sharp_classes_FieldDeclaration(
    ) {
        super(
        );
        this.attributess = new ArrayList<>();
        this.modifiers = new ArrayList<>();
    }

    public c_sharp_classes_FieldDeclaration(
        ArrayList<Attributes> attributess,        ArrayList<Modifier> modifiers    ) {
        this.attributess = attributess;
        this.modifiers = modifiers;
    }


    public List<Attributes> getAttributess() {
        return attributess;
    }

    public void addAttributes(Attributes attributes) {
        this.attributess.add(attributes);
    }
    public List<Modifier> getModifiers() {
        return modifiers;
    }

    public void addModifier(Modifier modifier) {
        this.modifiers.add(modifier);
    }

}