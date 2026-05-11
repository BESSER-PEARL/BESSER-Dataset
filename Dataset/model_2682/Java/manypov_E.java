





import java.util.List;
import java.util.ArrayList;

public class manypov_E extends Named {






    private List<manypov_F> manypov_fs;




    private manypov_A manypov_a;


    public manypov_E(
    ) {
        super(
        );
        this.manypov_fs = new ArrayList<>();
    }

    public manypov_E(
        ArrayList<manypov_F> manypov_fs    ) {
        this.manypov_fs = manypov_fs;
    }


    public List<manypov_F> getManypov_fs() {
        return manypov_fs;
    }

    public void addManypov_f(Manypov_f manypov_f) {
        this.manypov_fs.add(manypov_f);
    }
    public manypov_A getManypov_a() {
        return manypov_a;
    }

    public void setManypov_a(manypov_A manypov_a) {
        this.manypov_a = manypov_a;
    }

}