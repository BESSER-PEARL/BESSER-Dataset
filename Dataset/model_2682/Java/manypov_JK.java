





import java.util.List;
import java.util.ArrayList;

public class manypov_JK extends Named {






    private manypov_J manypov_j;




    private List<manypov_K> manypov_ks;


    public manypov_JK(
    ) {
        super(
        );
        this.manypov_ks = new ArrayList<>();
    }

    public manypov_JK(
        ArrayList<manypov_K> manypov_ks    ) {
        this.manypov_ks = manypov_ks;
    }


    public manypov_J getManypov_j() {
        return manypov_j;
    }

    public void setManypov_j(manypov_J manypov_j) {
        this.manypov_j = manypov_j;
    }
    public List<manypov_K> getManypov_ks() {
        return manypov_ks;
    }

    public void addManypov_k(Manypov_k manypov_k) {
        this.manypov_ks.add(manypov_k);
    }

}