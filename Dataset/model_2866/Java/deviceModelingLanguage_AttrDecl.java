





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_AttrDecl extends Accessor, MemberDecl {

    private String attributeName;



    public deviceModelingLanguage_AttrDecl(
        String attributeName    ) {
        super(
        );
        this.attributeName = attributeName;
    }


    public String getAttributename() {
        return attributeName;
    }

    public void setAttributename(String attributeName) {
        this.attributeName = attributeName;
    }


}