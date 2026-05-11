





import java.util.List;
import java.util.ArrayList;

public class henshin_text_Model  {






    private List<henshin_text_ModelElement> henshin_text_modelelements;


    public henshin_text_Model(
    ) {
        this.henshin_text_modelelements = new ArrayList<>();
    }

    public henshin_text_Model(
        ArrayList<henshin_text_ModelElement> henshin_text_modelelements    ) {
        this.henshin_text_modelelements = henshin_text_modelelements;
    }


    public List<henshin_text_ModelElement> getHenshin_text_modelelements() {
        return henshin_text_modelelements;
    }

    public void addHenshin_text_modelelement(Henshin_text_modelelement henshin_text_modelelement) {
        this.henshin_text_modelelements.add(henshin_text_modelelement);
    }

}