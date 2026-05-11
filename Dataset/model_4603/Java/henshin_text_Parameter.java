





import java.util.List;
import java.util.ArrayList;

public class henshin_text_Parameter  {

    private String kind;
    private String name;





    private henshin_text_ModelElement henshin_text_modelelement;


    public henshin_text_Parameter(
        String kind,        String name    ) {
        this.kind = kind;
        this.name = name;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public henshin_text_ModelElement getHenshin_text_modelelement() {
        return henshin_text_modelelement;
    }

    public void setHenshin_text_modelelement(henshin_text_ModelElement henshin_text_modelelement) {
        this.henshin_text_modelelement = henshin_text_modelelement;
    }

}