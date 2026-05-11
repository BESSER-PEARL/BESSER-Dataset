





import java.util.List;
import java.util.ArrayList;

public class henshin_text_LoopUnit extends UnitElement {






    private List<henshin_text_UnitElement> henshin_text_unitelements;


    public henshin_text_LoopUnit(
    ) {
        super(
        );
        this.henshin_text_unitelements = new ArrayList<>();
    }

    public henshin_text_LoopUnit(
        ArrayList<henshin_text_UnitElement> henshin_text_unitelements    ) {
        this.henshin_text_unitelements = henshin_text_unitelements;
    }


    public List<henshin_text_UnitElement> getHenshin_text_unitelements() {
        return henshin_text_unitelements;
    }

    public void addHenshin_text_unitelement(Henshin_text_unitelement henshin_text_unitelement) {
        this.henshin_text_unitelements.add(henshin_text_unitelement);
    }

}