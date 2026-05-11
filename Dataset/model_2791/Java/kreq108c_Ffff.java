





import java.util.List;
import java.util.ArrayList;

public class kreq108c_Ffff extends Gggg {

    private String id;





    private List<kreq108c_Eeee> kreq108c_eeees;




    private kreq108c_Ffff kreq108c_ffff;




    private kreq108c_Cccc kreq108c_cccc;


    public kreq108c_Ffff(
        String id    ) {
        super(
        );
        this.id = id;
        this.kreq108c_eeees = new ArrayList<>();
    }

    public kreq108c_Ffff(
        String id        ArrayList<kreq108c_Eeee> kreq108c_eeees    ) {
        this.id = id;
        this.kreq108c_eeees = kreq108c_eeees;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<kreq108c_Eeee> getKreq108c_eeees() {
        return kreq108c_eeees;
    }

    public void addKreq108c_eeee(Kreq108c_eeee kreq108c_eeee) {
        this.kreq108c_eeees.add(kreq108c_eeee);
    }
    public kreq108c_Ffff getKreq108c_ffff() {
        return kreq108c_ffff;
    }

    public void setKreq108c_ffff(kreq108c_Ffff kreq108c_ffff) {
        this.kreq108c_ffff = kreq108c_ffff;
    }
    public kreq108c_Cccc getKreq108c_cccc() {
        return kreq108c_cccc;
    }

    public void setKreq108c_cccc(kreq108c_Cccc kreq108c_cccc) {
        this.kreq108c_cccc = kreq108c_cccc;
    }

}