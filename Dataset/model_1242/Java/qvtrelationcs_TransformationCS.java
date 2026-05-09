





import java.util.List;
import java.util.ArrayList;

public class qvtrelationcs_TransformationCS extends ClassCS {






    private List<qvtrelationcs_ModelDeclCS> qvtrelationcs_modeldeclcss;




    private qvtrelationcs_PathNameCS qvtrelationcs_pathnamecs;




    private List<qvtrelationcs_QueryCS> qvtrelationcs_querycss;




    private qvtrelationcs_TopLevelCS qvtrelationcs_toplevelcs;




    private List<qvtrelationcs_KeyDeclCS> qvtrelationcs_keydeclcss;




    private List<qvtrelationcs_RelationCS> qvtrelationcs_relationcss;


    public qvtrelationcs_TransformationCS(
    ) {
        super(
        );
        this.qvtrelationcs_modeldeclcss = new ArrayList<>();
        this.qvtrelationcs_querycss = new ArrayList<>();
        this.qvtrelationcs_keydeclcss = new ArrayList<>();
        this.qvtrelationcs_relationcss = new ArrayList<>();
    }

    public qvtrelationcs_TransformationCS(
        ArrayList<qvtrelationcs_ModelDeclCS> qvtrelationcs_modeldeclcss,        ArrayList<qvtrelationcs_QueryCS> qvtrelationcs_querycss,        ArrayList<qvtrelationcs_KeyDeclCS> qvtrelationcs_keydeclcss,        ArrayList<qvtrelationcs_RelationCS> qvtrelationcs_relationcss    ) {
        this.qvtrelationcs_modeldeclcss = qvtrelationcs_modeldeclcss;
        this.qvtrelationcs_querycss = qvtrelationcs_querycss;
        this.qvtrelationcs_keydeclcss = qvtrelationcs_keydeclcss;
        this.qvtrelationcs_relationcss = qvtrelationcs_relationcss;
    }


    public List<qvtrelationcs_ModelDeclCS> getQvtrelationcs_modeldeclcss() {
        return qvtrelationcs_modeldeclcss;
    }

    public void addQvtrelationcs_modeldeclcs(Qvtrelationcs_modeldeclcs qvtrelationcs_modeldeclcs) {
        this.qvtrelationcs_modeldeclcss.add(qvtrelationcs_modeldeclcs);
    }
    public qvtrelationcs_PathNameCS getQvtrelationcs_pathnamecs() {
        return qvtrelationcs_pathnamecs;
    }

    public void setQvtrelationcs_pathnamecs(qvtrelationcs_PathNameCS qvtrelationcs_pathnamecs) {
        this.qvtrelationcs_pathnamecs = qvtrelationcs_pathnamecs;
    }
    public List<qvtrelationcs_QueryCS> getQvtrelationcs_querycss() {
        return qvtrelationcs_querycss;
    }

    public void addQvtrelationcs_querycs(Qvtrelationcs_querycs qvtrelationcs_querycs) {
        this.qvtrelationcs_querycss.add(qvtrelationcs_querycs);
    }
    public qvtrelationcs_TopLevelCS getQvtrelationcs_toplevelcs() {
        return qvtrelationcs_toplevelcs;
    }

    public void setQvtrelationcs_toplevelcs(qvtrelationcs_TopLevelCS qvtrelationcs_toplevelcs) {
        this.qvtrelationcs_toplevelcs = qvtrelationcs_toplevelcs;
    }
    public List<qvtrelationcs_KeyDeclCS> getQvtrelationcs_keydeclcss() {
        return qvtrelationcs_keydeclcss;
    }

    public void addQvtrelationcs_keydeclcs(Qvtrelationcs_keydeclcs qvtrelationcs_keydeclcs) {
        this.qvtrelationcs_keydeclcss.add(qvtrelationcs_keydeclcs);
    }
    public List<qvtrelationcs_RelationCS> getQvtrelationcs_relationcss() {
        return qvtrelationcs_relationcss;
    }

    public void addQvtrelationcs_relationcs(Qvtrelationcs_relationcs qvtrelationcs_relationcs) {
        this.qvtrelationcs_relationcss.add(qvtrelationcs_relationcs);
    }

}