





import java.util.List;
import java.util.ArrayList;

public class mydsl_B  {






    private List<mydsl_D> mydsl_ds;




    private mydsl_A mydsl_a;


    public mydsl_B(
    ) {
        this.mydsl_ds = new ArrayList<>();
    }

    public mydsl_B(
        ArrayList<mydsl_D> mydsl_ds    ) {
        this.mydsl_ds = mydsl_ds;
    }


    public List<mydsl_D> getMydsl_ds() {
        return mydsl_ds;
    }

    public void addMydsl_d(Mydsl_d mydsl_d) {
        this.mydsl_ds.add(mydsl_d);
    }
    public mydsl_A getMydsl_a() {
        return mydsl_a;
    }

    public void setMydsl_a(mydsl_A mydsl_a) {
        this.mydsl_a = mydsl_a;
    }

}