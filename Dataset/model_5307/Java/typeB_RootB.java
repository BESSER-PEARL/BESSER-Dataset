





import java.util.List;
import java.util.ArrayList;

public class typeB_RootB  {






    private List<typeB_ElementB> typeb_elementbs;




    private List<typeB_DefinitionB> typeb_definitionbs;


    public typeB_RootB(
    ) {
        this.typeb_elementbs = new ArrayList<>();
        this.typeb_definitionbs = new ArrayList<>();
    }

    public typeB_RootB(
        ArrayList<typeB_ElementB> typeb_elementbs,        ArrayList<typeB_DefinitionB> typeb_definitionbs    ) {
        this.typeb_elementbs = typeb_elementbs;
        this.typeb_definitionbs = typeb_definitionbs;
    }


    public List<typeB_ElementB> getTypeb_elementbs() {
        return typeb_elementbs;
    }

    public void addTypeb_elementb(Typeb_elementb typeb_elementb) {
        this.typeb_elementbs.add(typeb_elementb);
    }
    public List<typeB_DefinitionB> getTypeb_definitionbs() {
        return typeb_definitionbs;
    }

    public void addTypeb_definitionb(Typeb_definitionb typeb_definitionb) {
        this.typeb_definitionbs.add(typeb_definitionb);
    }

}