





import java.util.List;
import java.util.ArrayList;

public class MARTE_Alloc_Allocate  {

    private String nature;
    private String kind;



    public MARTE_Alloc_Allocate(
        String nature,        String kind    ) {
        this.nature = nature;
        this.kind = kind;
    }


    public String getNature() {
        return nature;
    }

    public void setNature(String nature) {
        this.nature = nature;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}