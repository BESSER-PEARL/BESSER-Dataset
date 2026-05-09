





import java.util.List;
import java.util.ArrayList;

public class LabelDefinition  {






    private gastm_LabeledStatement gastm_labeledstatement;




    private gastm_LabelAccess gastm_labelaccess;




    private sastm_RDBTableReference sastm_rdbtablereference;


    public LabelDefinition(
    ) {
    }



    public gastm_LabeledStatement getGastm_labeledstatement() {
        return gastm_labeledstatement;
    }

    public void setGastm_labeledstatement(gastm_LabeledStatement gastm_labeledstatement) {
        this.gastm_labeledstatement = gastm_labeledstatement;
    }
    public gastm_LabelAccess getGastm_labelaccess() {
        return gastm_labelaccess;
    }

    public void setGastm_labelaccess(gastm_LabelAccess gastm_labelaccess) {
        this.gastm_labelaccess = gastm_labelaccess;
    }
    public sastm_RDBTableReference getSastm_rdbtablereference() {
        return sastm_rdbtablereference;
    }

    public void setSastm_rdbtablereference(sastm_RDBTableReference sastm_rdbtablereference) {
        this.sastm_rdbtablereference = sastm_rdbtablereference;
    }

}