





import java.util.List;
import java.util.ArrayList;

public class moba_MobaServer extends MobaApplicationFeature {

    private String urlString;
    private String name;





    private List<moba_MobaREST> moba_mobarests;




    private moba_MobaAuthorization moba_mobaauthorization;




    private moba_MobaServer moba_mobaserver;




    private moba_MobaConstant moba_mobaconstant;


    public moba_MobaServer(
        String urlString,        String name    ) {
        super(
        );
        this.urlString = urlString;
        this.name = name;
        this.moba_mobarests = new ArrayList<>();
    }

    public moba_MobaServer(
        String urlString,        String name        ArrayList<moba_MobaREST> moba_mobarests    ) {
        this.urlString = urlString;
        this.name = name;
        this.moba_mobarests = moba_mobarests;
    }

    public String getUrlstring() {
        return urlString;
    }

    public void setUrlstring(String urlString) {
        this.urlString = urlString;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<moba_MobaREST> getMoba_mobarests() {
        return moba_mobarests;
    }

    public void addMoba_mobarest(Moba_mobarest moba_mobarest) {
        this.moba_mobarests.add(moba_mobarest);
    }
    public moba_MobaAuthorization getMoba_mobaauthorization() {
        return moba_mobaauthorization;
    }

    public void setMoba_mobaauthorization(moba_MobaAuthorization moba_mobaauthorization) {
        this.moba_mobaauthorization = moba_mobaauthorization;
    }
    public moba_MobaServer getMoba_mobaserver() {
        return moba_mobaserver;
    }

    public void setMoba_mobaserver(moba_MobaServer moba_mobaserver) {
        this.moba_mobaserver = moba_mobaserver;
    }
    public moba_MobaConstant getMoba_mobaconstant() {
        return moba_mobaconstant;
    }

    public void setMoba_mobaconstant(moba_MobaConstant moba_mobaconstant) {
        this.moba_mobaconstant = moba_mobaconstant;
    }

}