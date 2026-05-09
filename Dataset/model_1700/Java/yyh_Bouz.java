





import java.util.List;
import java.util.ArrayList;

public class yyh_Bouz extends Baz {

    private String bil;





    private List<yyh_Zing> yyh_zings;


    public yyh_Bouz(
        String bil    ) {
        super(
        );
        this.bil = bil;
        this.yyh_zings = new ArrayList<>();
    }

    public yyh_Bouz(
        String bil        ArrayList<yyh_Zing> yyh_zings    ) {
        this.bil = bil;
        this.yyh_zings = yyh_zings;
    }

    public String getBil() {
        return bil;
    }

    public void setBil(String bil) {
        this.bil = bil;
    }

    public List<yyh_Zing> getYyh_zings() {
        return yyh_zings;
    }

    public void addYyh_zing(Yyh_zing yyh_zing) {
        this.yyh_zings.add(yyh_zing);
    }

}