





import java.util.List;
import java.util.ArrayList;

public class moba_MobaEntityIndex  {

    private boolean unique;
    private String name;





    private List<moba_MobaEntityAttribute> moba_mobaentityattributes;




    private moba_MobaEntity moba_mobaentity;


    public moba_MobaEntityIndex(
        boolean unique,        String name    ) {
        this.unique = unique;
        this.name = name;
        this.moba_mobaentityattributes = new ArrayList<>();
    }

    public moba_MobaEntityIndex(
        boolean unique,        String name        ArrayList<moba_MobaEntityAttribute> moba_mobaentityattributes    ) {
        this.unique = unique;
        this.name = name;
        this.moba_mobaentityattributes = moba_mobaentityattributes;
    }

    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<moba_MobaEntityAttribute> getMoba_mobaentityattributes() {
        return moba_mobaentityattributes;
    }

    public void addMoba_mobaentityattribute(Moba_mobaentityattribute moba_mobaentityattribute) {
        this.moba_mobaentityattributes.add(moba_mobaentityattribute);
    }
    public moba_MobaEntity getMoba_mobaentity() {
        return moba_mobaentity;
    }

    public void setMoba_mobaentity(moba_MobaEntity moba_mobaentity) {
        this.moba_mobaentity = moba_mobaentity;
    }

}