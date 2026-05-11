





import java.util.List;
import java.util.ArrayList;

public class henshin_text_IteratedUnit extends UnitElement {






    private henshin_text_Expression henshin_text_expression;




    private List<henshin_text_UnitElement> henshin_text_unitelements;


    public henshin_text_IteratedUnit(
    ) {
        super(
        );
        this.henshin_text_unitelements = new ArrayList<>();
    }

    public henshin_text_IteratedUnit(
        ArrayList<henshin_text_UnitElement> henshin_text_unitelements    ) {
        this.henshin_text_unitelements = henshin_text_unitelements;
    }


    public henshin_text_Expression getHenshin_text_expression() {
        return henshin_text_expression;
    }

    public void setHenshin_text_expression(henshin_text_Expression henshin_text_expression) {
        this.henshin_text_expression = henshin_text_expression;
    }
    public List<henshin_text_UnitElement> getHenshin_text_unitelements() {
        return henshin_text_unitelements;
    }

    public void addHenshin_text_unitelement(Henshin_text_unitelement henshin_text_unitelement) {
        this.henshin_text_unitelements.add(henshin_text_unitelement);
    }

}