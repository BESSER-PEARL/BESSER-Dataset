





import java.util.List;
import java.util.ArrayList;

public class Air_Conditioners  {

    private int ACID;





    private List<HomeAppliances> homeappliancess;


    public Air_Conditioners(
        int ACID    ) {
        this.ACID = ACID;
        this.homeappliancess = new ArrayList<>();
    }

    public Air_Conditioners(
        int ACID        ArrayList<HomeAppliances> homeappliancess    ) {
        this.ACID = ACID;
        this.homeappliancess = homeappliancess;
    }

    public int getAcid() {
        return ACID;
    }

    public void setAcid(int ACID) {
        this.ACID = ACID;
    }

    public List<HomeAppliances> getHomeappliancess() {
        return homeappliancess;
    }

    public void addHomeappliances(Homeappliances homeappliances) {
        this.homeappliancess.add(homeappliances);
    }

}