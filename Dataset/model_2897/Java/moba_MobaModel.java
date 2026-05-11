





import java.util.List;
import java.util.ArrayList;

public class moba_MobaModel extends MobaFriendsAble {

    private String copyright;





    private List<moba_MobaModelFeature> moba_mobamodelfeatures;


    public moba_MobaModel(
        String copyright    ) {
        super(
        );
        this.copyright = copyright;
        this.moba_mobamodelfeatures = new ArrayList<>();
    }

    public moba_MobaModel(
        String copyright        ArrayList<moba_MobaModelFeature> moba_mobamodelfeatures    ) {
        this.copyright = copyright;
        this.moba_mobamodelfeatures = moba_mobamodelfeatures;
    }

    public String getCopyright() {
        return copyright;
    }

    public void setCopyright(String copyright) {
        this.copyright = copyright;
    }

    public List<moba_MobaModelFeature> getMoba_mobamodelfeatures() {
        return moba_mobamodelfeatures;
    }

    public void addMoba_mobamodelfeature(Moba_mobamodelfeature moba_mobamodelfeature) {
        this.moba_mobamodelfeatures.add(moba_mobamodelfeature);
    }

}