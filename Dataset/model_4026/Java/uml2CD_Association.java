





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Association extends NamedElement {

    private String isDerived;



    public uml2CD_Association(
        String isDerived    ) {
        super(
        );
        this.isDerived = isDerived;
    }


    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }


}