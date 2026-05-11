





import java.util.List;
import java.util.ArrayList;

public class oogen_OOForEach extends OOStatement {






    private List<oogen_OOStatement> oogen_oostatements;




    private oogen_OOVariable oogen_oovariable;




    private oogen_OOVariable oogen_oovariable;


    public oogen_OOForEach(
    ) {
        super(
        );
        this.oogen_oostatements = new ArrayList<>();
    }

    public oogen_OOForEach(
        ArrayList<oogen_OOStatement> oogen_oostatements    ) {
        this.oogen_oostatements = oogen_oostatements;
    }


    public List<oogen_OOStatement> getOogen_oostatements() {
        return oogen_oostatements;
    }

    public void addOogen_oostatement(Oogen_oostatement oogen_oostatement) {
        this.oogen_oostatements.add(oogen_oostatement);
    }
    public oogen_OOVariable getOogen_oovariable() {
        return oogen_oovariable;
    }

    public void setOogen_oovariable(oogen_OOVariable oogen_oovariable) {
        this.oogen_oovariable = oogen_oovariable;
    }
    public oogen_OOVariable getOogen_oovariable() {
        return oogen_oovariable;
    }

    public void setOogen_oovariable(oogen_OOVariable oogen_oovariable) {
        this.oogen_oovariable = oogen_oovariable;
    }

}