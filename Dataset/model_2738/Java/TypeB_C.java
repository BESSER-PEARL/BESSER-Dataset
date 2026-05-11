





import java.util.List;
import java.util.ArrayList;

public class TypeB_C  {

    private String name;





    private TypeB_CDescription typeb_cdescription;




    private TypeB_A typeb_a;


    public TypeB_C(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public TypeB_CDescription getTypeb_cdescription() {
        return typeb_cdescription;
    }

    public void setTypeb_cdescription(TypeB_CDescription typeb_cdescription) {
        this.typeb_cdescription = typeb_cdescription;
    }
    public TypeB_A getTypeb_a() {
        return typeb_a;
    }

    public void setTypeb_a(TypeB_A typeb_a) {
        this.typeb_a = typeb_a;
    }

}