





import java.util.List;
import java.util.ArrayList;

public class henshin_text_List  {






    private henshin_text_PriorityUnit henshin_text_priorityunit;




    private henshin_text_IndependentUnit henshin_text_independentunit;




    private List<henshin_text_UnitElement> henshin_text_unitelements;


    public henshin_text_List(
    ) {
        this.henshin_text_unitelements = new ArrayList<>();
    }

    public henshin_text_List(
        ArrayList<henshin_text_UnitElement> henshin_text_unitelements    ) {
        this.henshin_text_unitelements = henshin_text_unitelements;
    }


    public henshin_text_PriorityUnit getHenshin_text_priorityunit() {
        return henshin_text_priorityunit;
    }

    public void setHenshin_text_priorityunit(henshin_text_PriorityUnit henshin_text_priorityunit) {
        this.henshin_text_priorityunit = henshin_text_priorityunit;
    }
    public henshin_text_IndependentUnit getHenshin_text_independentunit() {
        return henshin_text_independentunit;
    }

    public void setHenshin_text_independentunit(henshin_text_IndependentUnit henshin_text_independentunit) {
        this.henshin_text_independentunit = henshin_text_independentunit;
    }
    public List<henshin_text_UnitElement> getHenshin_text_unitelements() {
        return henshin_text_unitelements;
    }

    public void addHenshin_text_unitelement(Henshin_text_unitelement henshin_text_unitelement) {
        this.henshin_text_unitelements.add(henshin_text_unitelement);
    }

}