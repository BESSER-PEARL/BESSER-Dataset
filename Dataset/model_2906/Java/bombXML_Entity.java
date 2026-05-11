





import java.util.List;
import java.util.ArrayList;

public class bombXML_Entity extends Type {

    private boolean abstract;





    private List<bombXML_Feature> bombxml_features;


    public bombXML_Entity(
        boolean abstract    ) {
        super(
        );
        this.abstract = abstract;
        this.bombxml_features = new ArrayList<>();
    }

    public bombXML_Entity(
        boolean abstract        ArrayList<bombXML_Feature> bombxml_features    ) {
        this.abstract = abstract;
        this.bombxml_features = bombxml_features;
    }

    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }

    public List<bombXML_Feature> getBombxml_features() {
        return bombxml_features;
    }

    public void addBombxml_feature(Bombxml_feature bombxml_feature) {
        this.bombxml_features.add(bombxml_feature);
    }

}