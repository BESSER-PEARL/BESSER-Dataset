





import java.util.List;
import java.util.ArrayList;

public class myDsl_Property  {

    private String name;





    private myDsl_GeneralEntity mydsl_generalentity;




    private myDsl_Type mydsl_type;


    public myDsl_Property(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_GeneralEntity getMydsl_generalentity() {
        return mydsl_generalentity;
    }

    public void setMydsl_generalentity(myDsl_GeneralEntity mydsl_generalentity) {
        this.mydsl_generalentity = mydsl_generalentity;
    }
    public myDsl_Type getMydsl_type() {
        return mydsl_type;
    }

    public void setMydsl_type(myDsl_Type mydsl_type) {
        this.mydsl_type = mydsl_type;
    }

}