





import java.util.List;
import java.util.ArrayList;

public class essentialOCLCST_PathNameCS extends TypeLiteralExpCS, TypeCS {






    private List<essentialOCLCST_SimpleNameCS> essentialoclcst_simplenamecss;


    public essentialOCLCST_PathNameCS(
    ) {
        super(
        );
        this.essentialoclcst_simplenamecss = new ArrayList<>();
    }

    public essentialOCLCST_PathNameCS(
        ArrayList<essentialOCLCST_SimpleNameCS> essentialoclcst_simplenamecss    ) {
        this.essentialoclcst_simplenamecss = essentialoclcst_simplenamecss;
    }


    public List<essentialOCLCST_SimpleNameCS> getEssentialoclcst_simplenamecss() {
        return essentialoclcst_simplenamecss;
    }

    public void addEssentialoclcst_simplenamecs(Essentialoclcst_simplenamecs essentialoclcst_simplenamecs) {
        this.essentialoclcst_simplenamecss.add(essentialoclcst_simplenamecs);
    }

}