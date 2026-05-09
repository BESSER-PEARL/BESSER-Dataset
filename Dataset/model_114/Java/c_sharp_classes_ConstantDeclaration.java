





import java.util.List;
import java.util.ArrayList;

public class c_sharp_classes_ConstantDeclaration extends ClassMemberDeclaration {






    private List<Modifier> modifiers;




    private List<Attributes> attributess;


    public c_sharp_classes_ConstantDeclaration(
    ) {
        super(
        );
        this.modifiers = new ArrayList<>();
        this.attributess = new ArrayList<>();
    }

    public c_sharp_classes_ConstantDeclaration(
        ArrayList<Modifier> modifiers,        ArrayList<Attributes> attributess    ) {
        this.modifiers = modifiers;
        this.attributess = attributess;
    }


    public List<Modifier> getModifiers() {
        return modifiers;
    }

    public void addModifier(Modifier modifier) {
        this.modifiers.add(modifier);
    }
    public List<Attributes> getAttributess() {
        return attributess;
    }

    public void addAttributes(Attributes attributes) {
        this.attributess.add(attributes);
    }

}