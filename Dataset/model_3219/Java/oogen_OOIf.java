





import java.util.List;
import java.util.ArrayList;

public class oogen_OOIf extends OOConditionalStatement {






    private List<oogen_OOStatement> oogen_oostatements;




    private oogen_OOIf oogen_ooif;


    public oogen_OOIf(
    ) {
        super(
        );
        this.oogen_oostatements = new ArrayList<>();
    }

    public oogen_OOIf(
        ArrayList<oogen_OOStatement> oogen_oostatements    ) {
        this.oogen_oostatements = oogen_oostatements;
    }


    public List<oogen_OOStatement> getOogen_oostatements() {
        return oogen_oostatements;
    }

    public void addOogen_oostatement(Oogen_oostatement oogen_oostatement) {
        this.oogen_oostatements.add(oogen_oostatement);
    }
    public oogen_OOIf getOogen_ooif() {
        return oogen_ooif;
    }

    public void setOogen_ooif(oogen_OOIf oogen_ooif) {
        this.oogen_ooif = oogen_ooif;
    }

}