





import java.util.List;
import java.util.ArrayList;

public class typeA_ElementA  {

    private String name;





    private typeA_RootA typea_roota;


    public typeA_ElementA(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public typeA_RootA getTypea_roota() {
        return typea_roota;
    }

    public void setTypea_roota(typeA_RootA typea_roota) {
        this.typea_roota = typea_roota;
    }

}