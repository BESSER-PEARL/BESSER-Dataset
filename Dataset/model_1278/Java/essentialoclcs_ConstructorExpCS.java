





import java.util.List;
import java.util.ArrayList;

public class essentialoclcs_ConstructorExpCS extends NamedExpCS {

    private String value;





    private List<essentialoclcs_ConstructorPartCS> essentialoclcs_constructorpartcss;


    public essentialoclcs_ConstructorExpCS(
        String value    ) {
        super(
        );
        this.value = value;
        this.essentialoclcs_constructorpartcss = new ArrayList<>();
    }

    public essentialoclcs_ConstructorExpCS(
        String value        ArrayList<essentialoclcs_ConstructorPartCS> essentialoclcs_constructorpartcss    ) {
        this.value = value;
        this.essentialoclcs_constructorpartcss = essentialoclcs_constructorpartcss;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public List<essentialoclcs_ConstructorPartCS> getEssentialoclcs_constructorpartcss() {
        return essentialoclcs_constructorpartcss;
    }

    public void addEssentialoclcs_constructorpartcs(Essentialoclcs_constructorpartcs essentialoclcs_constructorpartcs) {
        this.essentialoclcs_constructorpartcss.add(essentialoclcs_constructorpartcs);
    }

}