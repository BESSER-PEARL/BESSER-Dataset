





import java.util.List;
import java.util.ArrayList;

public class majordomo_Room extends Extendable {

    private String name;





    private majordomo_Majordomo majordomo_majordomo;


    public majordomo_Room(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public majordomo_Majordomo getMajordomo_majordomo() {
        return majordomo_majordomo;
    }

    public void setMajordomo_majordomo(majordomo_Majordomo majordomo_majordomo) {
        this.majordomo_majordomo = majordomo_majordomo;
    }

}