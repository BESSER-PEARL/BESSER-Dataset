





import java.util.List;
import java.util.ArrayList;

public class myDsl_Transaction  {

    private String type;





    private myDsl_SpecialEntity mydsl_specialentity;


    public myDsl_Transaction(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public myDsl_SpecialEntity getMydsl_specialentity() {
        return mydsl_specialentity;
    }

    public void setMydsl_specialentity(myDsl_SpecialEntity mydsl_specialentity) {
        this.mydsl_specialentity = mydsl_specialentity;
    }

}