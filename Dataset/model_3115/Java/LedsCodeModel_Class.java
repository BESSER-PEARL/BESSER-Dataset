





import java.util.List;
import java.util.ArrayList;

public class LedsCodeModel_Class extends AbstractClass {

    private boolean abstract;
    private String stereotypeClass;





    private List<LedsCodeModel_Class> ledscodemodel_classs;


    public LedsCodeModel_Class(
        boolean abstract,        String stereotypeClass    ) {
        super(
        );
        this.abstract = abstract;
        this.stereotypeClass = stereotypeClass;
        this.ledscodemodel_classs = new ArrayList<>();
    }

    public LedsCodeModel_Class(
        boolean abstract,        String stereotypeClass        ArrayList<LedsCodeModel_Class> ledscodemodel_classs    ) {
        this.abstract = abstract;
        this.stereotypeClass = stereotypeClass;
        this.ledscodemodel_classs = ledscodemodel_classs;
    }

    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public String getStereotypeclass() {
        return stereotypeClass;
    }

    public void setStereotypeclass(String stereotypeClass) {
        this.stereotypeClass = stereotypeClass;
    }

    public List<LedsCodeModel_Class> getLedscodemodel_classs() {
        return ledscodemodel_classs;
    }

    public void addLedscodemodel_class(Ledscodemodel_class ledscodemodel_class) {
        this.ledscodemodel_classs.add(ledscodemodel_class);
    }

}