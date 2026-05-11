





import java.util.List;
import java.util.ArrayList;

public class typeB_RootB  {






    private List<typeB_DefinitionB> typeb_definitionbs;


    public typeB_RootB(
    ) {
        this.typeb_definitionbs = new ArrayList<>();
    }

    public typeB_RootB(
        ArrayList<typeB_DefinitionB> typeb_definitionbs    ) {
        this.typeb_definitionbs = typeb_definitionbs;
    }


    public List<typeB_DefinitionB> getTypeb_definitionbs() {
        return typeb_definitionbs;
    }

    public void addTypeb_definitionb(Typeb_definitionb typeb_definitionb) {
        this.typeb_definitionbs.add(typeb_definitionb);
    }

}