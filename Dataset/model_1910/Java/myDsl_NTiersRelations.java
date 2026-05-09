





import java.util.List;
import java.util.ArrayList;

public class myDsl_NTiersRelations  {

    private String name;





    private myDsl_NTierTarget mydsl_ntiertarget;




    private myDsl_NTierSource mydsl_ntiersource;


    public myDsl_NTiersRelations(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_NTierTarget getMydsl_ntiertarget() {
        return mydsl_ntiertarget;
    }

    public void setMydsl_ntiertarget(myDsl_NTierTarget mydsl_ntiertarget) {
        this.mydsl_ntiertarget = mydsl_ntiertarget;
    }
    public myDsl_NTierSource getMydsl_ntiersource() {
        return mydsl_ntiersource;
    }

    public void setMydsl_ntiersource(myDsl_NTierSource mydsl_ntiersource) {
        this.mydsl_ntiersource = mydsl_ntiersource;
    }

}