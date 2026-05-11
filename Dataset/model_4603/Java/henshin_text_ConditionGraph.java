





import java.util.List;
import java.util.ArrayList;

public class henshin_text_ConditionGraph  {

    private String name;





    private henshin_text_Formula henshin_text_formula;


    public henshin_text_ConditionGraph(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public henshin_text_Formula getHenshin_text_formula() {
        return henshin_text_formula;
    }

    public void setHenshin_text_formula(henshin_text_Formula henshin_text_formula) {
        this.henshin_text_formula = henshin_text_formula;
    }

}