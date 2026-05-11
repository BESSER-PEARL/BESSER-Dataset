





import java.util.List;
import java.util.ArrayList;

public class shr5Management_MetaType extends PriorityCategorie {

    private int specialPoints;





    private shr5Management_KarmaGenerator shr5management_karmagenerator;




    private shr5Management_Shr5Generator shr5management_shr5generator;


    public shr5Management_MetaType(
        int specialPoints    ) {
        super(
        );
        this.specialPoints = specialPoints;
    }


    public int getSpecialpoints() {
        return specialPoints;
    }

    public void setSpecialpoints(int specialPoints) {
        this.specialPoints = specialPoints;
    }

    public shr5Management_KarmaGenerator getShr5management_karmagenerator() {
        return shr5management_karmagenerator;
    }

    public void setShr5management_karmagenerator(shr5Management_KarmaGenerator shr5management_karmagenerator) {
        this.shr5management_karmagenerator = shr5management_karmagenerator;
    }
    public shr5Management_Shr5Generator getShr5management_shr5generator() {
        return shr5management_shr5generator;
    }

    public void setShr5management_shr5generator(shr5Management_Shr5Generator shr5management_shr5generator) {
        this.shr5management_shr5generator = shr5management_shr5generator;
    }

}