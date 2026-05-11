





import java.util.List;
import java.util.ArrayList;

public class sPLOT2CoCo_ParentChildConstraint  {






    private sPLOT2CoCo_FM splot2coco_fm;




    private List<sPLOT2CoCo_TreeConstraint> splot2coco_treeconstraints;




    private sPLOT2CoCo_Feature splot2coco_feature;


    public sPLOT2CoCo_ParentChildConstraint(
    ) {
        this.splot2coco_treeconstraints = new ArrayList<>();
    }

    public sPLOT2CoCo_ParentChildConstraint(
        ArrayList<sPLOT2CoCo_TreeConstraint> splot2coco_treeconstraints    ) {
        this.splot2coco_treeconstraints = splot2coco_treeconstraints;
    }


    public sPLOT2CoCo_FM getSplot2coco_fm() {
        return splot2coco_fm;
    }

    public void setSplot2coco_fm(sPLOT2CoCo_FM splot2coco_fm) {
        this.splot2coco_fm = splot2coco_fm;
    }
    public List<sPLOT2CoCo_TreeConstraint> getSplot2coco_treeconstraints() {
        return splot2coco_treeconstraints;
    }

    public void addSplot2coco_treeconstraint(Splot2coco_treeconstraint splot2coco_treeconstraint) {
        this.splot2coco_treeconstraints.add(splot2coco_treeconstraint);
    }
    public sPLOT2CoCo_Feature getSplot2coco_feature() {
        return splot2coco_feature;
    }

    public void setSplot2coco_feature(sPLOT2CoCo_Feature splot2coco_feature) {
        this.splot2coco_feature = splot2coco_feature;
    }

}