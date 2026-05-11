





import java.util.List;
import java.util.ArrayList;

public class henshin_text_Call extends UnitElement {






    private henshin_text_ModelElement henshin_text_modelelement;




    private List<henshin_text_Parameter> henshin_text_parameters;


    public henshin_text_Call(
    ) {
        super(
        );
        this.henshin_text_parameters = new ArrayList<>();
    }

    public henshin_text_Call(
        ArrayList<henshin_text_Parameter> henshin_text_parameters    ) {
        this.henshin_text_parameters = henshin_text_parameters;
    }


    public henshin_text_ModelElement getHenshin_text_modelelement() {
        return henshin_text_modelelement;
    }

    public void setHenshin_text_modelelement(henshin_text_ModelElement henshin_text_modelelement) {
        this.henshin_text_modelelement = henshin_text_modelelement;
    }
    public List<henshin_text_Parameter> getHenshin_text_parameters() {
        return henshin_text_parameters;
    }

    public void addHenshin_text_parameter(Henshin_text_parameter henshin_text_parameter) {
        this.henshin_text_parameters.add(henshin_text_parameter);
    }

}