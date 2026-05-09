





import java.util.List;
import java.util.ArrayList;

public class yyg_Bouz extends Baz {

    private String bil;





    private List<yyg_Zing> yyg_zings;


    public yyg_Bouz(
        String bil    ) {
        super(
        );
        this.bil = bil;
        this.yyg_zings = new ArrayList<>();
    }

    public yyg_Bouz(
        String bil        ArrayList<yyg_Zing> yyg_zings    ) {
        this.bil = bil;
        this.yyg_zings = yyg_zings;
    }

    public String getBil() {
        return bil;
    }

    public void setBil(String bil) {
        this.bil = bil;
    }

    public List<yyg_Zing> getYyg_zings() {
        return yyg_zings;
    }

    public void addYyg_zing(Yyg_zing yyg_zing) {
        this.yyg_zings.add(yyg_zing);
    }

}