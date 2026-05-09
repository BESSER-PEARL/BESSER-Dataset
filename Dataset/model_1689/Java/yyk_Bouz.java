





import java.util.List;
import java.util.ArrayList;

public class yyk_Bouz extends Baz {

    private String bil;





    private List<yyk_Zing> yyk_zings;


    public yyk_Bouz(
        String bil    ) {
        super(
        );
        this.bil = bil;
        this.yyk_zings = new ArrayList<>();
    }

    public yyk_Bouz(
        String bil        ArrayList<yyk_Zing> yyk_zings    ) {
        this.bil = bil;
        this.yyk_zings = yyk_zings;
    }

    public String getBil() {
        return bil;
    }

    public void setBil(String bil) {
        this.bil = bil;
    }

    public List<yyk_Zing> getYyk_zings() {
        return yyk_zings;
    }

    public void addYyk_zing(Yyk_zing yyk_zing) {
        this.yyk_zings.add(yyk_zing);
    }

}